from rickaym.pyminecraft import Mod

import org.apache.logging.log4j.LogManager as LogManager

from ext import ExtensionClass, SecondExtensionClass
from more_ext import MoreExt

@Mod(mod_id="abc")
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

    def register(self):
        """
        Method to register things into appropriate registries
        """
        print "Main register called."
        ExtensionClass.register()
        SecondExtensionClass.register()
        MoreExt.register()