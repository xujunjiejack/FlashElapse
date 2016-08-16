import unittest
from utils.util import open_dialog_for_path

class MyTestCase(unittest.TestCase):
    def test_file_dialog(self):
        path = open_dialog_for_path(path_type="f")
        print(path)
        target_path = "/Users/xu/Desktop/Set Home Page.png"

        self.assertIsNotNone(path)
        self.assertEqual(path,target_path,"It's not file path")

    def test_dic_dialog(self):
        path = open_dialog_for_path(path_type="d")
        print(path)
        target_path = "/Users/xu/Desktop"

        self.assertIsNotNone(path)
        self.assertEqual(path,target_path,"It's not directory path")

if __name__ == '__main__':
    unittest.main()
