import unittest
from user_commands.cmd_manager import CommandManager
from user_request_channel.command_line_channel import CommandLineChannel

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cmd_manager = CommandManager()
        self.cmdl = CommandLineChannel(self.cmd_manager)


    def call_back_test(self,data_dict):
        self.test_string = "Response"


    def test_print_prompt(self):
        self.cmdl.start_listening(self.call_back_test)
        self.assertEqual(self.test_string,"Response")


if __name__ == '__main__':
    unittest.main()
