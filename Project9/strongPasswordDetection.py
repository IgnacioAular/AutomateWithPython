

# Developer: Ignacio Aular
# ignacio345@gmail.com
# Tue Jun 14, 7:48 PM

# Strong Password Detection:

# Write a function that uses regular expressions to make sure the password
# string it is passed is strong. A strong password is defined as one that is at
# least eight characters long, contains both uppercase and lowercase charac-
# ters, and has at least one digit. You may need to test the string against mul-
# tiple regex patterns to validate its strength.

import re

def passwordStrength(psw):
    """ Check for at least eight characters long, contains both
         uppercase and lowercase characters, and has at least one
         digit.
         Args: password (str): password as string
         Returns: strong (bool): True if password is strong else False
    """

    eightLong = re.compile(r'[\w\d\s\W\D\S]{8,}')  # check for 8 chars
    upperCase = re.compile(r'[A-Z]+')                   # check for upper cases
    lowerCase = re.compile(r'[a-z]+')                    # check for lower cases
    oneOrMoreDigit = re.compile(r'\d+')                # check for one or more digits
    
    if not eightLong.search(psw):
        return False
    elif not upperCase.search(psw):
        return False
    elif not lowerCase.search(psw):
        return False
    elif not oneOrMoreDigit.search(psw):
        return False
    return True    

if __name__ == "__main__":
    psw = 'B/qwerty8#-'
    print(passwordStrength(psw))
