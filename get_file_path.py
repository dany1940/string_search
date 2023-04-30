from pathlib import Path
import re
from arguments import Arguments


class File:
    """Get the file path from the command line."""

    def __init__(self):
        self.args = Arguments().get_arguments()
        self.sentence = self.__read_file()

    def __check_file_type(self, file_path):
        """Check if the file is a txt file."""
        if file_path.suffix == ".txt":
            return True
        else:
            return False

    def __get_file_path(self):
        # walk the target directory and take the name of the files
        args = self.args
        file_path = Path(args.D)
        check_type = self.__check_file_type(file_path)
        if check_type:
            return file_path
        else:
            print("The file is not a txt file!")
            raise SystemExit(1)

    def __read_file(self):
        """Read the file and return a list of sentences with no new line characters."""
        """Get the arguments from the command line."""
        """returns a list of sentences with no new line characters."""
        # pasing the arguments to the parser
        file_path = self.__get_file_path()
        sentences = []
        try:
            with open(file_path, "r") as file:
                lines = file.read().splitlines()
                for sentence in lines:
                    sentence = re.sub("[^A-Za-z]+", " ", sentence)
                    sentence = sentence.strip()
                    sentence = sentence.replace("\t", "")
                    if sentence:
                        sentences.append(sentence)
        except IndexError:
            print("The index is out of range!")
            raise SystemExit(1)
        except FileNotFoundError:
            print("The file does not exist!")
            raise SystemExit(1)
        except PermissionError:
            print("You do not have permission to access this file!")
            raise SystemExit(1)
        return sentences

    def __getitem__(self, index):
        return self.sentence[index]
