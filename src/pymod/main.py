import rickaym.pyforge.Mod as Mod
import rickaym.pyforge.PyModLoadingContext as PyModLoadingContext
import org.apache.logging.log4j.LogManager as LogManager
import constants

from mod_items import ModItems, ModBlocks

@Mod(mod_id=constants.MOD_ID)
class MyMod:
    """
    Exemplary implementation of the Mod class.

    Identified using the @Mod decorator and an appropriate
    mod id.

    It's a bad idea to decorate multiple classes with
    this decorator and expose both of them publicly.
    """

    def __init__(self):
        self.LOGGER = LogManager.getLogger()
        self.LOGGER.info("Pymod has been loaded in!")

        eventBus = PyModLoadingContext.get().getModEventBus()
        ModItems.register(eventBus)
        ModBlocks.register(eventBus)
