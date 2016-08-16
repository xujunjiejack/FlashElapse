from user_commands.command_api import Command, CommandCMDLInput,ExecutableCommand

import os
from user_setting import get_photo_path


class MakeVideoCmd(Command):

    def __init__(self):
        super(MakeVideoCmd,self).__init__()

    def _set_cmd_name_(self):
        return "Make video"

    def _set_cmdl_channel_class_(self):
        return MakeVideoCMDL

    def decode(self, data_dict, delegate = None):
        return MakeVideoExeCmd(data_dict,delegate)
    
    

class MakeVideoCMDL(CommandCMDLInput):

    def __init__(self):
        super(MakeVideoCMDL,self).__init__()

    def _react_for_data_(self):
        x = input("Please enter the frame you want")

        # invalidate
        # return
        data_dict = {"frame": x}
        return data_dict

    def get_prompt_line(self):
        return "Put all of the photos into video"


class MakeVideoExeCmd(ExecutableCommand):
    def __init__(self,data_dict=None,delegate=None):
        super(MakeVideoExeCmd, self).__init__(data_dict,delegate)
        
    def _exe_(self):
        os.system(
            "avconv -r 10  -i /home/pi/Desktop/timelapse/myimage_%04d.jpg -r 10 "
            "-vcodec libx264 -crf 20 -g 15 /home/pi/Desktop/timelapse/timelapse.mp4")

        pass
