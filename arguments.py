import argparse
from pathlib import Path


def get_arguments():
    """Get the arguments from the command line."""

    parser = argparse.ArgumentParser(description="Find patterns in a txt file")

    parser.add_argument(
        type=Path,
        dest="P",
        help="No path specified!",
    )
    args = parser.parse_args()
    path_to_file = Path(args.P)

    if not path_to_file.exists():
        print("The path does not exist!")
        raise SystemExit(1)

    return args
