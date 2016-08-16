import unittest
from user_setting import project_name


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.string = "Hello World"

        #If you need to assign a module value, you need to use global keyword
        global project_name

        project_name = self.string

    def test_outer_scope(self):

        self.assertEqual(project_name,self.string)

if __name__ == '__main__':
    unittest.main()
