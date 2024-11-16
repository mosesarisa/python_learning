
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s * 50 
    if exclaim:
        result = result + '!!!'
    return result
print(repeat('hello', False))
print(repeat('hello', True))