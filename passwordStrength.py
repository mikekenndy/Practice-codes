# test code to determine whether password entered is strong enough

import re

def strongPW(password):
    if len(password) < 8:
        return False
    hasUpper = False
    hasLower = False
    hasDigit = False
    for letter in password:
        if letter.isupper():
            hasUpper = True
        if letter.islower():
            hasLower = True
        if letter.isdigit():
            hasDigit = True
    if hasUpper and hasLower and hasDigit:
        return True
    return False

print('Password must contain'
      '\t8 total characters'
      '\t1 upper case character'
      '\t1 lower case character'
      '\t1 number')
print('Input password: ', end= '')
userPW = input()
while(not strongPW(userPW)):
    print('Password does not meet criteria.')
    print('Input password: ', end='')
    userPW = input()
print('Password set')