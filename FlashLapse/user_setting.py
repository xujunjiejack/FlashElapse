# photo_path will be set in the photo_path
photo_path = ""

# the project_name will be set in the main after initializing the project
project_name = ""

# the camera that get only used in the camera
camera = None


def set_camera(a_camera):
    global camera
    camera = a_camera


def get_camera():
    return camera


def set_project_name(name):
    global project_name
    project_name = name


def get_project_name():
    return project_name


def set_photo_path(path):
    global photo_path
    photo_path = path


def get_photo_path():
    global photo_path
    return photo_path
