class EmptyListException(Exception):
    """Raised when the list is empty"""

    SystemExit(1)
    pass


class LongPatternException(Exception):
    """Raised when the pattern is longer than the sentences"""

    SystemExit(1)
    pass


class MissingPermissionException(Exception):
    """Raised when the user does not have permission to access the file"""

    SystemExit(1)
    pass


class WronFileExtensionException(Exception):
    """Raised when the file is not a txt file"""

    SystemExit(1)
    pass

class MissingPatternException(Exception):
    """Raised when the pattern is missing"""

    SystemExit(1)
    pass
class EmptyPathException(Exception):
    """Raised when the file is empty"""

    SystemExit(1)
    pass
class EmptyFileException(Exception):
    """Raised when the file is empty"""

    SystemExit(1)
    pass

