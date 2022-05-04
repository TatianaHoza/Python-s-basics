import os

#def scan_dir(dir, level = 0):
#    for name in os.listdir(dir):
#        path = os.path.join(dir, name)
#       if os.path.isfile(path):
#            print(' '*level, path)
#        else:
#            print(' '*level, path)
#            scan_dir(path, level+1)

#scan_dir('.')
for root, dirs, files in os.walk('.'):
#    file_size = os.lstat(files).st_size
    print(root, dirs, files)


