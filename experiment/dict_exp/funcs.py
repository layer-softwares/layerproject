

def stringParser(string):
    """
    Parse a string to a list of strings.
    """
    if string is None:
        return None
    if type(string) is list:
        return string
    if type(string) is str:
        return [string]
    raise TypeError("stringParser: string must be a string or a list of strings")


def stringListParser(stringList):
    """
    Parse a list of strings to a list of lists of strings.
    """
    if stringList is None:
        return None
    if type(stringList) is list:
        return [stringParser(string) for string in stringList]
    raise TypeError("stringListParser: stringList must be a list of strings")


def tokenParser(token):
    """
    Parse a string to a list of tokens.
    """
    if token is None:
        return None
    if type(token) is list:
        return token
    if type(token) is str:
        return token.split()
    raise TypeError("tokenParser: token must be a string or a list of strings")