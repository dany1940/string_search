#!/usr/bin/env solution
from arguments import get_arguments
from pattern import get_pattern
from pattern import find_pattern
from read_file import read_file









if __name__ == '__main__':
    """Main function. Here the program starts."""
    """Read the file and return a list of sentences with no new line characters."""
    sentences = read_file(get_arguments()) # get the arguments from the command line
    pattern = get_pattern(sentences) # get a list of all possible substrings of the pattern
    find_pattern(pattern, sentences[ : -1]) # find the pattern in the sentences less the last entry which is the actual pattern

