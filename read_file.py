import re



def read_file(file_path):
    """Read the file and return a list of sentences with no new line characters."""
    """Get the arguments from the command line."""
    """returns a list of sentences with no new line characters."""
     #pasing the arguments to the parser
    sentences = []
    try:
          with open(file_path, 'r') as file:
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
