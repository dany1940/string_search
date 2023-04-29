import re




def get_pattern(sentence):
    """get a list of all possible substrings of the pattern"""
    pattern = sentence[-1]
    return pattern



def find_pattern(pattern, sentences):
    """Find the pattern in the sentences."""
    sentence = ("[{0}]".format(
                       ''.join(map(str, sentences))))
    for sentence in sentences:
            if re.search(pattern, sentence):
                print (("[{0}]".format(
                       ''.join(map(str, sentence)))))
            else:
                print("No match found!")
                raise SystemExit(1)

