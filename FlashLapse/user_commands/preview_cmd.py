from user_commands.command_api import Command,ExecutableCommand,CommandCMDLInput
from tkinter import Tk

class PreviewCmd(Command):
    def __init__(self):
        super(PreviewCmd,self).__init__()

    def _set_cmd_name_(self):
        return "Preview"

    def _set_cmdl_channel_class_(self):
        return PreviewCMDLChannel

    def decode(self,data_dict,delegate=None):
        return PreviewExeCmd()


class PreviewExeCmd(ExecutableCommand):
    def __init__(self,data_dict=None,delegate=None):
        super(PreviewExeCmd,self).__init__(data_dict,delegate)
        from user_setting import get_camera
        self.camera = get_camera()

    def _exe_(self):
        '''The actual execute code for doing command. Every exception it throws will
        be thrown to execute to be a command runtime error. This error handling has
        been delegated to the execute(). Outsider should not use this method for run
        Developer needs to inheritance this method for the command to run
        '''
        self.camera.start_preview()
        # TODO: let's change the scheme for the preview. That is using a Tkinter
        # to receive the non ascii key to provide good avoidance
        # One thing is that tkinter might not be available. So we need to
        # include it before we can actually make it work.

        root = Tk()
        # bind the key here
        self._bind_keys_(root)

        # force the user to focus on the root controller
        root.focus_force()
        root.mainloop()

    def _bind_keys_(self, root):
        self._bind_arrow_key_(root)
        self._bind_escape_key(root)
        pass

    def _bind_arrow_key_(self,root):
        def flip_horizontal(event):
            self.camera.hflip = not self.camera.hflip
            #print("The left has been pressed")
            pass

        def flip_vertial(event):
            self.camera.vflip = not self.camera.vflip
            #print("The up has been pressed")
            pass

        root.bind("<Left>", flip_horizontal)
        root.bind("<Right>", flip_horizontal)
        root.bind("<Up>", flip_vertial)
        root.bind("<Down>", flip_vertial)

    def _bind_escape_key(self,root):

        def end_root(event, root):
            root.destroy()
            self.camera.stop_preview()

        root.bind("<Escape>", lambda event: end_root(event, root))

class PreviewCMDLChannel(CommandCMDLInput):
    def __init__(self):
        super(PreviewCMDLChannel,self).__init__()

    def get_prompt_line(self):
        return "Preview"

    def _require_extra_argument_(self):
        return False
