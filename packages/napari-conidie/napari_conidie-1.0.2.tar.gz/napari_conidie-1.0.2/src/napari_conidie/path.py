import os.path

homedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

base_dir = "."

def get_base_dir():
    return os.path.abspath(os.path.join(homedir, base_dir))

def get_models_dir():
    return os.path.join(get_base_dir(), "napari_conidie")

def get_ilastik_exe():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, "ilastik_txt.txt")