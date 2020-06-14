#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

# Developer: Ignacio Aular
# ignacio345@gmail.com
# Tue Sun 14, 6:45 AM

import pyperclip, re

# Step 1: Create a Regex for Phone Numbers
# First, you have to create a regular expression to search for phone numbers.
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                  # area code
(\s|-|\.)?                                 # separator
(\d{3})                                  # first 3 digits
(\s|-|\.)                                   # separator
(\d{4})                                  # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)


# Step 2: Create a Regex for Email Addresses
# You will also need a regular expression that can match email addresses.
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+              # username
@                                        # @ symbol
[a-zA-Z0-9.-]+                     # domain name
(\.[a-zA-Z]{2,4})                  # dot-something
)''', re.VERBOSE)


# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

























