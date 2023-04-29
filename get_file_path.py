from pathlib import Path



def check_file_type(file_path):
    """Check if the file is a txt file."""
    if file_path.suffix == ".txt":
        return True
    else:
        return False



def get_file_path(args):
    # walk the target directory and take the name of the file
            file_path = Path(args.D)
            if check_file_type(file_path):
                return file_path
            else:
                print("The file is not a txt file!")
                raise SystemExit(1)


