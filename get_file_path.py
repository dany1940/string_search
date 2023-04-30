from pathlib import Path
import re
from arguments import Arguments
import os
from exceptions import EmptyListException
from exceptions import LongPatternException
from exceptions import MissingPermissionException
from exceptions import WronFileExtensionException
from exceptions import EmptyPathException
from exceptions import EmptyFileException


class File:
    """Get the file path from the command line."""

    args = Arguments().get_arguments()
    file_path = Path(args.D)
    file_name = os.path.basename(file_path)
    file_suffix = file_path.suffix

    def __init__(self):
        self.sentence = self.__read_file()

    def __check_file_type(self):
        """Check if the file is a txt file."""
        if self.file_path.suffix == ".txt":
            return True
        else:
            return False

    def __get_file_path(self):
        # walk the target directory and take the name of the files
        check_type = self.__check_file_type()
        if check_type:
            return self.file_path
        else:
            raise WronFileExtensionException(self.file_suffix)

    def __read_file(self):
        """Read the file and return a list of sentences with no new line characters."""
        """returns a list of sentences with no new line characters."""
        # pasing the arguments to the parser
        file_path = self.__get_file_path()
        if not os.access(file_path, os.R_OK):
            raise MissingPermissionException(self.file_name)
        elif not os.path.getsize(file_path):
            raise EmptyPathException(self.file_name)
        sentences = []

        try:
            with open(file_path, "r") as file:
                lines = file.read().splitlines()
                if not lines:
                    raise EmptyFileException(self.file_name)
                for sentence in lines:
                    sentence = re.sub("[^A-Za-z]+", " ", sentence)
                    sentence = sentence.strip()
                    sentence = sentence.replace("\t", "")
                    if sentence:
                        sentences.append(sentence)
        except MissingPermissionException:
            print(f"You do not have permission to access {self.file_name}!")
        if not sentences:
            print(f"The are no words in the  {self.file_name}!")
            raise EmptyListException(self.file_name)
        elif len(max(sentences[:-1], key=len)) < len(sentences[-1]):
            print(
                f"The pattern '{sentences[-1]}' of lenght {len(sentences[-1])} is too long and will not be found in the sentences\n"
                "hence no additional search will be performed."
            )
            raise LongPatternException(len(sentences[-1]))
        return sentences

    def __getitem__(self, index):
        return self.sentence[index]
