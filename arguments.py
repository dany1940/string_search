import argparse


class Arguments:
    """Get the arguments from the command line."""

    def __arguments(self):
        """Get the arguments from the command line.

        Returns:
            args: the arguments from the command line
        """
        parser = argparse.ArgumentParser(description="Find patterns in a txt file")
        parser.add_argument(
            dest="D",
            nargs="?",
            type=str,
            default="",
            help="Need to specify a directory to read the files from",
        )
        args = parser.parse_args()

        return args

    @staticmethod
    def get_arguments():
        """Get the arguments from the command line.

        Returns:
            args: the arguments from the command line
        """
        args = Arguments().__arguments()
        return args
