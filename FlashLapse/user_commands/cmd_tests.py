import unittest
from user_commands.take_photo_command import TakePhotoExeCmd
from threading import Thread
from time import sleep

class MyTestCase(unittest.TestCase):

    def setUp(self):
        data_dict = {"CMD_NAME":"Take photo", "time_interval":4, "time_exp":1 }
        self.tp_cmd = TakePhotoExeCmd(data_dict=data_dict)

        pass

    def test_something(self):
        self.tp_cmd._exe_()
        #sleep(60)

        self.assertEqual(True,True)

if __name__ == '__main__':
    unittest.main()
