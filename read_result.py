import os
import re
import mmap
from arguments import Arguments
from pathlib import Path
from exceptions import EmptyFileException
from exceptions import WronFileExtensionException
from exceptions import MissingPermissionException
from exceptions import EmptyPathException


class File:
    """_summary_

    Raises:
        WronFileExtensionException: if a wrong file extension is passed as argument
        MissingPermissionException: if the user does not have permission to access the file
        EmptyPathException: if the path to the is empty
        EmptyFileException: if the file is empty

    Returns:
        None: Print the sentences with the pattern
    """

    args = Arguments().get_arguments()
    file_path = Path(args.D)
    file_name = os.path.basename(file_path)
    file_suffix = file_path.suffix

    def __init__(self):
        """
        This is the constructor of the class.
        In this case, it will read the file and get the pattern.
        """
        self.sentence = self.__read_file_and_get_pattern()

    def __check_file_type(self):
        """Check if the file is a txt file.

        Returns:
            bool: True if the file is a txt file, False otherwise
        """
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

    def __sanitize_result(self, line):
        """Sanitize the result.

        Args:
            line (str): the line to sanitize
        """
        line = re.sub(
            "[^A-Za-zÀ-ÿáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕàèìòùÀÈÌÒÙåÅæÆœŒçÇðÐøØß]+",
            " ",
            line,
            flags=re.I,
        )
        line = line.replace("\t", "")
        line = line.strip()
        print(("[{0}]".format("".join(map(str, line)))))

    def __read_file_and_get_pattern(self):
        """Read the file and return a list of sentences with no new line characters.

        Raises:
            MissingPermissionException: if the user does not have permission to access the file
            EmptyPathException: if the path to the is empty
            EmptyFileException: if the file is empty
        """
        # pasing the arguments to the parser
        file_path = self.__get_file_path()
        if not os.access(file_path, os.R_OK):
            raise MissingPermissionException(self.file_name)
        elif not os.path.getsize(file_path):
            raise EmptyPathException(self.file_name)
        elif os.path.getsize(file_path) == 0:
            print(f"The file {self.file_name} is empty!")
            raise EmptyFileException(self.file_name)
        try:
            with open(file_path, "rb+") as file:  # read the last line of the file
                file.seek(-2, os.SEEK_END)  # go to the end of the file
                while file.read(1) != b"\n":  # Until EOL is found...
                    file.seek(
                        -2, os.SEEK_CUR
                    )  # ...jump back the read byte plus one more.

                    if (
                        file.tell() == 0
                    ):  # So we will not be out of the file if we met the beginning
                        break
                pattern = file.readline().decode()  # Read last line.
                re_genre = (
                    r"{}".format(pattern).encode().strip()
                )  # convert the pattern to bytes
                size_bytes_pattern = len(re_genre)  # get the size of the pattern
                file_stat = os.stat(file_path)  # get the size of the file
                file_size = file_stat.st_size  # get the size of the file
                new_file_size = file_size - (
                    size_bytes_pattern + 1
                )  # get the new size of the file
                with mmap.mmap(
                    file.fileno(),
                    new_file_size,
                    prot=mmap.PROT_READ,  # open the file with mmap
                ) as mmap_obj:
                    # read the file with mmap
                    for line in iter(mmap_obj.readline, rb""):
                        result = bool(
                            re.search(re_genre, line, re.IGNORECASE)
                        )  # search the pattern in the file
                        if result:
                            line = line.decode("utf-8")  # decode the line
                            self.__sanitize_result(line)  # sanitize the line
        except MissingPermissionException:
            print(f"You do not have permission to access {self.file_name}!")
