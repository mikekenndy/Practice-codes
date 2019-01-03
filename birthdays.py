# dictionarys and lists

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        print('Terminating...')
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('No birthday information for ' + name)
        print('Enter ' + name +'\'s birthday: ', end='')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')