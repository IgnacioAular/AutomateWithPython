
# Developer: Ignacio Aular
# ignacio345@gmail.com
# Tue Jun 12, 11:00 PM

#
# Open a new file editor window and save the program as pw.py. You need
# to start the program with a #! (shebang) line and should also write a
# comment that briefly describes the program. Since you want to associate
# each account’s name with its password, you can store these as strings in
# a dictionary.
#

#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

#
# The command line arguments will be stored in the variable sys.argv.
# The first item in the sys.argv list should always be a string containing
# the program’s filename ('pw.py'), and the second item should be the
# first command line argument. For this program, this argument is the
# name of the account whose password you want. Since the command line
# argument is mandatory, you display a usage message to the user if they
# forget to add it (that is, if the sys.argv list has fewer than two values in it).
#

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

#
# Now that the account name is stored as a string in the variable account, you
# need to see whether it exists in the PASSWORDS dictionary as a key. If so, you
# want to copy the key’s value to the clipboard using pyperclip.copy(). (Since
# you’re using the pyperclip module, you need to import it.) Note that you
# don’t actually need the account variable; you could just use sys.argv[1] every-
# where account is used in this program. But a variable named account is much
# more readable than something cryptic like sys.argv[1].
#

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

print('Your password is: ' + pyperclip.paste())

