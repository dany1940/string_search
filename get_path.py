import os



def get_file_path(args):
    file_path = []
    for root,dirs, paths in os.walk(args.P): # walk the target directory tree and store all of the file paths
        try:
           for path in paths:
              print(path)
              full_path = os.path.join(root,path) #print(full_path)
              file_path.append(full_path)
              print(file_path)
        except FileNotFoundError:
            print("The directory does not exist!")
            raise SystemExit(1)
    return file_path
