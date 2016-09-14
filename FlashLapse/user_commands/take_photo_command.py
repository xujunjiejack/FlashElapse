from user_commands.command_api import Command,ExecutableCommand,CommandCMDLInput
from time import sleep
from _thread import start_new_thread
from os import system
from utils.util import open_dialog_for_path
from user_setting import get_project_name,set_photo_path, get_photo_path
from utils.image_name import ImageName

class TakePhotoCmd(Command):
    def __init__(self):
        super(TakePhotoCmd,self).__init__()

    def _set_cmd_name_(self):
        return "Take photo"

    def _set_cmdl_channel_class_(self):
        return TakePhotoCMDLChannel

    def decode(self,data_dict,delegate=None):
        return TakePhotoExeCmd(data_dict,delegate)


class TakePhotoExeCmd(ExecutableCommand):
    def __init__(self,data_dict=None,delegate=None):
        super(TakePhotoExeCmd,self).__init__(data_dict,delegate)

    #		from __init__ import picamera,camera
    #		self.camera = camera

    def _exe_(self):
        '''The actual execute code for doing command. Every exception it throws will
        be thrown to execute to be a command runtime error. This error handling has
        been delegated to the execute(). Outsider should not use this method for run
        Developer needs to inheritance this method for the command to run
        '''

        photo_path = self.ask_photo_store_path()
        set_photo_path(photo_path)

        time_interval = self.data_dict['time_interval']
        time_exp = self.data_dict['time_exp']
        total_frame_num = (time_exp * 60 / time_interval)

        def take_photo(total_frame_num,time_interval,path,project_name):
            i = 0
            image_name = ImageName()
            while i < total_frame_num:
                sleep(time_interval)
                print("Taking photo %s / %s at %s" % (i,total_frame_num,path))
                print(image_name.get_image_name(number=i,directory_path=get_photo_path()))

                #self.camera.capture(image_name.get_image_name(number=i,directory_path=get_photo_path()))
                i += 1
            print("Done with taking photo, please check the folder")

        start_new_thread(take_photo,(int(total_frame_num),time_interval,
                                     photo_path,get_project_name()))

    def ask_photo_store_path(self):
        path = open_dialog_for_path(user_prompt="Please choose a directory to store photos"
                                    ,path_type="d")
        if path == None or path == "" :
            raise ValueError("No directory has been choosed to store the data")

        return path


class TakePhotoCMDLChannel(CommandCMDLInput):
    def __init__(self):
        super(TakePhotoCMDLChannel,self).__init__()

    def get_prompt_line(self):
        return "Take photo"

    def _react_for_data_(self):
        data_dict = {}

        def check_string_as_integer(string):
            try:
                num = int(string)
                return num
            except ValueError as e:
                raise UserInputError("Please enter an integer")

        def check_int_positive(num):
            if num <= 0:
                raise UserInputError("Frames per minute can't be negative or zero. ")

        def read_time_interval_console():

            while True:
                try:
                    time_interval = input(" How many seconds do you want between"
                                          " each photo: ")
                    time_interval = check_string_as_integer(time_interval)
                    check_int_positive(time_interval)
                    return time_interval

                except UserInputError as e:
                    print(e,"\nPlease try again.")

        def read_time_of_experiment():
            while True:
                try:
                    time_exp = input("Please enter the time length of actual"
                                     " experiment in minutes: ")
                    time_exp = check_string_as_integer(time_exp)
                    check_int_positive(time_exp)
                    return time_exp
                except UserInputError as e:
                    print(e,"\nPlease try again.")

        time_interval = read_time_interval_console()  # time_interval is interger
        time_exp = read_time_of_experiment()  # time_exp is interger
        print("time_interval: %s, time_exp: %s" % (time_interval,time_exp))
        data_dict['time_interval'] = time_interval
        data_dict['time_exp'] = time_exp
        return data_dict


class UserInputError(Exception):
    pass
