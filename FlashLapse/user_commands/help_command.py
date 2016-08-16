import sys
sys.path.insert(0,'/Users/xu/Desktop/Projects/FlashLapse/FlashLapse')
print(sys.path)

from user_commands.command_api import Command, CommandCMDLInput
from utils.common_exceptions import PrintHelpException

class HelpCmd(Command):

    def __init__(self):
        super(HelpCmd,self).__init__()

    def _set_cmd_name_(self):
        return "help"

    def _set_cmdl_channel_class_(self):
        return HelpCMDLInput


class HelpCMDLInput(CommandCMDLInput):
    def __init__(self):
        super(HelpCMDLInput,self).__init__()

    def _react_for_data_(self):
        raise PrintHelpException("Printing help")

    def get_prompt_line(self):
        return "Get user help"