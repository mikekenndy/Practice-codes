# fantasy inventory
"""Also an experiment with mult-line
    commenting using
    multiline string
"""

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, loot):
    for k in loot:
        if not str(k) in inventory:
            inventory[str(k)] = 1
        else:
            inventory[str(k)] += 1

player_1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print('Before')
displayInventory(player_1)
addToInventory(player_1, loot)
print('Loot added')
displayInventory(player_1)