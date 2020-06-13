
# Developer: Ignacio Aular
# ignacio345@gmail.com
# Tue Jun 13, 1:28 AM

#! python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

#
# Example:
#
# Input:
#
# Lists of animals
# Lists of aquarium life
# Lists of biologists by author abbreviation
# Lists of cultivars
#
# Output:
#
# * Lists of animals
# * Lists of aquarium life
# * Lists of biologists by author abbreviation
# * Lists of cultivars
#

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)):
    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

# Join the Modified Lines
text = '\n'.join(lines)

pyperclip.copy(text)

