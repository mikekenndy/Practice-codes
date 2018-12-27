# takes a list and returns the values separated by commas

def commas(list):
    temp = list
    retString = ''
    if(len(list) > 1):
        temp.insert(len(list) - 1, 'and')
    for i in list:
        retString += i + ', '
    retString = retString[0:len(retString)-2]
    return retString

# Get list from user
print('Input list items, press enter when done')
myStuff = []
i = 1;

while(True):
    print('Item ' + str(i) + ': ', end = '')
    i = i+1
    item = input()
    if(item == ''):
        break
    myStuff.append(item)

sortedList = commas(myStuff)
print(sortedList)