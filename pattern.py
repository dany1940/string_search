import re
from get_file_path import File


class Pattern:
    """Get the pattern from the command line."""
    def __init__(self):
        self.sentence = File()
        self.pattern = self.__get_pattern(self.sentence)
        self.find_pattern = self.__find_pattern()

    def __get_pattern(self, sentence):
        """get a list of all possible substrings of the pattern"""
        pattern = sentence[-1]
        if pattern == "\n":
            print("The pattern is empty!")
            raise SystemExit(1)
        else:
            return pattern



    def __find_pattern(self):
        """Find the pattern in the sentences."""
        """Strip the new line character from the pattern."""
        """returns a list of sentences with the pattern in square brackets."""
        """Removes the tabs and the new line characters from the sentences."""
        result = []
        pattern = self.pattern
        sentences = self.sentence[ : -1]
        for sentence in sentences:
            if  re.search(pattern, sentence, re.IGNORECASE):
                result.append(("[{0}]".format(
                        ''.join(map(str, sentence)))))
        if  not result:
            print("The pattern is not found!")
        else:
            print("The pattern is found in the following sentences:")
            for sentence in result:
                print(sentence)

    @staticmethod
    def get_solution():
        """Get the pattern from the command line."""
        solution = Pattern().__find_pattern()
        return solution




