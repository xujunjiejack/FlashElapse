# photo_path will be set in the photo_path
photo_path = ""

# the project_name will be set in the main after initializing the project
project_name = ""

# the camera will be set when the program is initialized
camera = None

def set_photo_path(path):
    global photo_path
    photo_path = path

def get_photo_path():
    global photo_path
    return photo_path