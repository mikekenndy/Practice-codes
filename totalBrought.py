#Practice with nested lists

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwich': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things brought')
print(' - Apples\t\t\t' + str(totalBrought(allGuests, 'apples')))
print(' - Cups\t\t\t\t' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes\t\t\t' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham sandwiches\t' + str(totalBrought(allGuests, 'ham sandwich')))
print(' - Apple Pies\t\t' + str(totalBrought(allGuests, 'apple pies')))