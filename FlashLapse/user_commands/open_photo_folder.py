from user_commands.command_api import Command, CommandCMDLInput
import os
from user_setting import get_photo_path

class OpenPhotoFolderCmd(Command):

    def __init__(self):
        super(OpenPhotoFolderCmd, self).__init__()

    def _set_cmd_name_(self):
        return "Open Photo Folder"

    def _set_cmdl_channel_class_(self):
        return OpenPhotoFolderCMDL

class OpenPhotoFolderCMDL(CommandCMDLInput):

    def __init__(self):
        super(OpenPhotoFolderCMDL,self).__init__()

    def _is_util_(self):
        return True

    def get_prompt_line(self):
        return "Open the folder where you store your photos"

    def _react_for_data_(self):
        '''You have to return {} at the end of the place'''
        photo_path = get_photo_path()
        if photo_path =="":
            print("Please taking photo before you can use this command")
        else:
            # this command is for Mac
            os.system("open %s" %photo_path)

            # Need the linux to be here
            # os.system("xdg-open %s" %photo_path)