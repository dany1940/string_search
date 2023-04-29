import argparse



def get_arguments():
    """Get the arguments from the command line."""
    parser = argparse.ArgumentParser(description="Find patterns in a txt file")
    parser.add_argument(
        dest="D",
        nargs="?",
        type=str,
        default="../string_search/test.txt",
        help="Need to specify a directory to read the files from",
    )
    args = parser.parse_args()

    return args
