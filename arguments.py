import argparse



def get_arguments():
    """Get the arguments from the command line."""
    parser = argparse.ArgumentParser(description="Find patterns in a txt file")

    parser.add_argument(
        dest="P",
        help="No path specified!",
    )
    args = parser.parse_args()
    return args
