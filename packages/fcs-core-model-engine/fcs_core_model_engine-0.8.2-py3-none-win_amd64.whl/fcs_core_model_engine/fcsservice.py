
from .geometrybuilder import GeometryBuilder
from .fcscore import ModelBuilder
from .fcslogger import FCSLogger

class BackendService(object):
    """
    Template class for hosting specific plugins.
    """

    def __init__(self, service_name: str):
        """
        Constructor.
        """
        self.service_name = service_name
        self.db: ModelBuilder
        self.gb: GeometryBuilder

    def set_existing_services(self, 
                              model_builder: ModelBuilder,
                              geometry_builder: GeometryBuilder,
                              logger: FCSLogger
                              ) -> None: 
        """
        To any backend service connect we pass on the instances of the main operators.
        """

        self.model_builder = model_builder
        self.geometry_builder = geometry_builder
        self.logger = logger

    def run_command(self, command_name: str, command_args: dict={}) -> dict | None:
        """
        Returns true, if the command was found and run (even if it failed).
        Return false otherwise.
        """

        self.logger.set_logging_context(self.service_name)
        result = None

        if command_name not in self.get_available_callbacks():
            self.logger.wrn(f'Request a command name that was not made available: {command_name}.')
            return {'Error' : f'Command name unavailable {command_name}'}

        try:
            command_ptr = getattr(self, command_name)
            result = command_ptr(command_args)
        except AttributeError as ex_atrr:
            self.logger.err(f'Probably could not find {command_name}! (Exception: {ex_atrr.args})')
        except Exception as ex:
            self.logger.err(f'Running command {command_name} failed: {ex.args}!')
        finally: 
            self.logger.set_logging_context('')

        return result

#--------------------------------------------------------------------------------------------------
# Pure virtual methods that require implementation
#--------------------------------------------------------------------------------------------------

    def get_available_callbacks(self, args: dict | None = None) -> list:
        """
        List of available callbacks to be forwarded to the listeners of the cloud application.
        """
        raise NotImplementedError("`get_available_callbacks` needs to be implemented in the base class!")
