import __init__
import sys, getopt
from rpb_controller import RpbController
from utils.util import open_dialog_for_path
from user_setting import project_name

def ask_project_name():
    project_name = input("Please enter your project name: ")
    if project_name.strip() == "":
        print("No project name provided, system quitting")
        sys.exit(2)
    return project_name

def main(argv):

    def read_input_source_from_cmd(argv):
        ''' get the input source from command line'''
        error_message = "Argument invalid, please check the help for further info"
        help_message = "Usage: python FlashLapse -i <inputs source: cmd, lan >"
        input_source_command = ["cmd","lan"]

        try:
            if len(argv) == 0:
                raise getopt.GetoptError("Please type in an argument")

            opts, args = getopt.getopt(argv, "hi:")

            # parse the argument
            for opt, args in opts:
                if opt == "-h":
                    print("Help message: "+ help_message)
                    sys.exit(2) #if the user print help, you need to rerun the program

                elif opt == "-i":
                    if args not in input_source_command:
                        raise getopt.GetoptError("Input source command not valid")
                    return args
                else:
                    raise getopt.GetoptError("Please type in argument")

        except getopt.GetoptError as e:
            print( e.msg + "\n" + error_message + "\n" +  help_message)
            sys.exit(2)


    #run the RpbController
    source = read_input_source_from_cmd(argv)

    global project_name
    project_name = ask_project_name()

    rpb_controller = RpbController(source)
    rpb_controller.run()

if __name__ == "__main__":
    main(sys.argv[1:])