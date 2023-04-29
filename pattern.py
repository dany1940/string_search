import re




def get_pattern(sentence):
    """get a list of all possible substrings of the pattern"""
    pattern = sentence[-1]
    return pattern



def find_pattern(pattern, sentences):
    """Find the pattern in the sentences."""
    result = []
    for sentence in sentences:
        if  re.search(pattern, sentence):
             result.append(("[{0}]".format(
                       ''.join(map(str, sentence)))))
    if  not result:
        print("The pattern is not found!")
    else:
        print("The pattern is found in the following sentences:")
        for sentence in result:
            print(sentence)




