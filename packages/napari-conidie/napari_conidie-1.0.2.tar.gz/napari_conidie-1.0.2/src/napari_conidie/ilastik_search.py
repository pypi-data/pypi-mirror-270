import os
import time
from pathlib import Path
import napari.utils.notifications as napari_not
class GetOutOfLoop( Exception ):
    pass

def ilastik_txt_search():
    dir_path1 = os.path.dirname(os.path.realpath(__file__))
    dir_path2 = Path(dir_path1).anchor
    pth_ilastik_txt = os.path.join(dir_path1,"ilastik_txt.txt")
    dir_path3 = Path(pth_ilastik_txt)

    if not dir_path3.exists():
        path_ilastik = None
        start_time = time.time()
        try:
            for root, dirs, files in os.walk(dir_path2):
                for file in files:
                    if 'ilastik' in file and file.endswith('.exe'):
                        path_ilastik = os.path.join(root,str(file))
                        raise GetOutOfLoop
        except GetOutOfLoop:
            pass
        print('TIME:',time.time() - start_time)


        if not dir_path3.exists():
            if path_ilastik!=None:
                f = open(pth_ilastik_txt, "w")
                f.write(path_ilastik)
                f.close()
            else:
                napari_not.show_warning('Ilastik not installed')
    else:
        print(pth_ilastik_txt,"already set")