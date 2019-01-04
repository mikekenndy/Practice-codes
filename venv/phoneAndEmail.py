#! python3
# phoneAndEmail.py - finds phone numbers and email addresses on the clipboard

import pyperclip, re

def getPhoneNumbers(text):
    phoneRegex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?      # area code
            (\s|-|\.)?              # separator
            \d{3}                   # first 3 digits
            (\s|-|\.)               # separator
            \d{4}                   # last 4 digits
            (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
            )''', re.VERBOSE)  # VERBOSE allows for comments within expression
    matches = []
    for numbers in phoneRegex.findall(text):
        matches.append(numbers[0])
    return matches

def getEmails(text):
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       # username
        @
        [a-zA-Z0-9.-]+          # domain name
        (\.[a-zA-Z]{2,4})       # dot-something
        )''', re.VERBOSE)
    matches = []
    for emails in emailRegex.findall(text):
        matches.append(emails[0])
    return matches

text = pyperclip.paste()

print('Coppied to clipboard:')
phoneNums = getPhoneNumbers(text)
mail = getEmails(text)

if len(phoneNums) > 0 or len(mail) > 0:
    toClipboard = ''
    print('\n'.join(phoneNums))
    toClipboard = ('\n'.join(phoneNums))
    print('\n'.join(mail))
    toClipboard += ('\n'.join(mail))
    # Copy results to keyboard
    pyperclip.copy(str(toClipboard))
else:
    print('\tNothing found.')