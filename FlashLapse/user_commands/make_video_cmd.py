from user_commands.command_api import Command, CommandCMDLInput,ExecutableCommand

import os

from user_request_channel.command_line_channel import UserInputError
from user_setting import get_photo_path, get_project_name
from utils.image_name import ImageName


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

        def check_string_as_integer(string):
            try:
                num = int(string)
                return num
            except ValueError as e:
                raise UserInputError("Please enter an integer")

        def check_int_positive(num):
            if num <= 0:
                raise UserInputError("Frames per minute can't be negative or zero. ")
            return num

        fps = input("Please enter the frames per second you want. Recommend 30 or 60:")
        fps = check_string_as_integer(fps)
        fps = check_int_positive(fps)

        # invalidate
        # return
        data_dict = {"fps": fps}
        return data_dict

    def get_prompt_line(self):
        return "Put all of the photos captured into video"


class MakeVideoExeCmd(ExecutableCommand):
    def __init__(self,data_dict=None,delegate=None):
        super(MakeVideoExeCmd, self).__init__(data_dict,delegate)

    def _exe_(self):

        # assume the fps exist
        fps = self.data_dict["fps"]
        image_name = ImageName()
        image_path = image_name.get_image_name(directory_path=get_photo_path())
        video_name = os.path.join(get_photo_path(),get_project_name()+".mp4")

        make_video_command = "avconv -r %s  -i %s -r %s -vcodec libx264" \
                             " -crf 20 -g 15 %s"%(fps, fps,image_path,video_name)

        print(make_video_command)
        #os.system(make_video_command)
