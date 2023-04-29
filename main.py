#!/usr/bin/env solution
from arguments import get_arguments
import re



def read_file(args):
    """Read the file and return a list of sentences with no new line characters."""
    path = args.P
    #file_size = os.path.getsize('nodata.txt')
    sentences = []
    try:
       with open(path, 'r') as file:
            lines = file.read().splitlines()
            for sentence in lines:
                sentence =  re.sub('[^A-Za-z]+', ' ', sentence)
                sentence = sentence.strip()
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

def get_all_patterns(sentence):
    """get a list of all possible substrings of the pattern"""
    pattern = sentence[-1]
    #list_of_substrings = ([pattern[i:j] for i in range(len(pattern)) for j in range(i + 1, len(pattern) + 1)])
    return pattern

def find_pattern(pattern, sentences):
    """Find the pattern in the sentences."""
    sentence = ("[{0}]".format(
                       ''.join(map(str, sentences))))
    for sentence in sentences:
            if re.search(pattern, sentence):
                print (("[{0}]".format(
                       ''.join(map(str, sentence)))))




if __name__ == '__main__':
    """Main function."""
    """Read the file and return a list of sentences with no new line characters."""
    sentences = read_file(get_arguments())
    pattern = get_all_patterns(sentences)
    find_pattern(pattern, sentences[ : -1])

