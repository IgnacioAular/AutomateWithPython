
# Developer: Ignacio Aular
# ignacio345@gmail.com
# Tue Jun 14, 11:20 PM

# Regex Version of strip():
#     
# Write a function that takes a string and does the same thing as the strip()
# string method. If no other arguments are passed other than the string to
# strip, then whitespace characters will be removed from the beginning and
# end of the string. Otherwise, the characters specified in the second argu-
# ment to the function will be removed from the string.

import re

def strip(text):
    """ Python's str.strip() method implemented using regex
    Args: text (str): text to strip of white space
    Returns: textStripped (str): text stripped of white space
    """
    stripStartRegex = re.compile(r'(^\s*)')
    stripEndRegex = re.compile(r'(\s*$)')

    textStartStripped = stripStartRegex.sub('', text)
    textStripped = stripEndRegex.sub('', textStartStripped)

    return textStripped

if __name__ == "__main__":
    text = ' test ffs   '
    print(strip(text))
