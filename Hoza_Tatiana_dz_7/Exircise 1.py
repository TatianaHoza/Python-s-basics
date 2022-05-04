import os

dir_name = os.path.join('--my_project', '--settings')
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
dir_name_2 = os.path.join('--my_project', '--mainapp')
if not os.path.exists(dir_name_2):
    os.makedirs(dir_name_2)
dir_name_3 = os.path.join('--my_project', '--adminapp')
if not os.path.exists(dir_name_3):
    os.makedirs(dir_name_3)
dir_name_4 = os.path.join('--my_project', '--authapp')
if not os.path.exists(dir_name_4):
    os.makedirs(dir_name_4)