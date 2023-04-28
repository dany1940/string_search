#!/usr/bin/env solution
from arguments import get_arguments
import re


def read_file(args):
    """Read the file and return a list of sentences with no new line characters."""
    path = args.P
    # file_size = os.path.getsize('nodata.txt')
    try:
        with open(path, "r") as file:
            sentence = file.read().splitlines()
    except IndexError:
        print("The index is out of range!")
        raise SystemExit(1)
    except FileNotFoundError:
        print("The file does not exist!")
        raise SystemExit(1)
    except PermissionError:
        print("You do not have permission to access this file!")
        raise SystemExit(1)
    return sentence


def get_all_patterns(read_file):
    """get a list of all possible substrings of the pattern"""
    pattern = read_file.pop()
    list_of_substrings = [
        pattern[i:j]
        for i in range(len(pattern))
        for j in range(i + 1, len(pattern) + 1)
    ]
    return list_of_substrings


def find_pattern(pattern, sentences):
    """Find the pattern in the sentences."""
    list_of_sentences = []
    for sentence in sentences:
        for pattern in pattern:
            if re.search(pattern, sentence):
                list_of_sentences.append(sentence)
    return list_of_sentences


if __name__ == "__main__":
    sentences = read_file(get_arguments())
    new_sentences = []
    for sentence in sentences:
        sentence = "".join(ch for ch in sentence if ch.isalpha())
        new_sentences.append(sentence)
    print(new_sentences)
    pattern = get_all_patterns(sentences)
