#!/usr/bin/env solution
from pattern import get_pattern
from pattern import find_pattern
from read_file import read_file
from get_path import get_file_path
from arguments import get_arguments









if __name__ == '__main__':
    """Main function. Here the program starts."""
    """Read the file and return a list of sentences with no new line characters."""
    args = get_arguments()
    path = get_file_path(args)
    sentences = read_file(path) # get the arguments from the command line
    pattern = get_pattern(sentences) # get a list of all possible substrings of the pattern
    find_pattern(pattern, sentences[ : -1]) # find the pattern in the sentences less the last entry which is the actual pattern


