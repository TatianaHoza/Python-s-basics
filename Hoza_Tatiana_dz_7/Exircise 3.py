import os
import shutil

dir_name = 'C:/Users/Vital/PycharmProjects/Python-s-basics/Hoza_Tatiana_dz_7/--my_project'
test = os.listdir(dir_name)
for item in test:
    if item.endswith('.html'):
        shutil.copy2(os.path.join(dir_name, item), '--templates')

