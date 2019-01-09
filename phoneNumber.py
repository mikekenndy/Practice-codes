# REGEX practice
# check whether input is a phone number #

import re

message = 'Call me at (415) 555-4242 tomorrow. If I\'m unavailable, 415-555-9999 is my office number.'

# # ? - section is optional
# phoneNum = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
# num = phoneNum.findall(message)
# print('Phone numberss:')
# for n in num:
#     print('\t' + str(n))

# # .* - matching everything
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Mike Last Name: Kennedy')
# print('Name: ' + mo.group(1) + ' ' + mo.group(2))

# # substitue method
# namesRegex = re.compile(r'Agent \w+')
# redacted = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# print(redacted)
#
# namesRegex = re.compile(r'Agent (\w)\w*')
# redacted = namesRegex.sub('\1****', 'Agent Alice told Agent Carol that Agent '
#                                     'Eve knew Agent Bob was a double agent.')
# print(redacted)

# complex regexes
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?      # area code
        (\s|-|\.)?              # separator
        \d{3}                   # first 3 digits
        (\s|-|\.)               # separator
        \d{4}                   # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
        )''', re.VERBOSE)   #VERBOSE allows for comments within expression
nums = phoneRegex.findall(message)
print('Message: ' + message)
print('Numbers found:')
for n in nums:
    print('\t' + n[0].strip())

# # . - the wildcard character
# # .I - case insensitive
# atRegex = re.compile(r'\w+at', re.I)
# words = atRegex.findall('The CAT in the hAt sat on the fLaT mat.')
# print('Words with \'at\':')
# for at in words:
#     print('\t' + at)

# # finding other characters
# #   d - number 0-9
# #   s - space, tab, newline
# #   w - letter, number, underscore
# xmaxRegex = re.compile(r'\d+\s\w+')
# days = xmaxRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, ' +
#                   '6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print('Found:')
# for thing in days:
#     print('\t' + thing)

# # * - match zero or more
# batRegex = re.compile(r'Bat(wo)*man')
# mo = batRegex.search('The Adventures of Batwowowowowoman')
# print(mo.group())

# # + - match ONE or more
# batRegex = re.compile(r'Bat(wo)+man')
# mo = batRegex.search('The Adventures of Batman')
# if mo == None:
#     print('None')
# else:
#     print(mo.group())

# # greedy - matches the longest string possible
# haRegex = re.compile(r'(Ha){3,5}')
# mo = haRegex.search('HaHaHaHaHa')
# print(mo.group())

# # non-greedy - matches shortest string possible
# non_greedy_haRegex = re.compile(r'(Ha){3,5}?')
# mo2 = non_greedy_haRegex.search('HaHaHaHaHa')
# print(mo2.group())