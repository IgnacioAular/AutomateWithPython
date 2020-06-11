
# Developer: Ignacio Aular
# ignacio345@gmail.com
# Tue Jun 11, 11:20 AM

# List to Dictionary Function for Fantasy Game Inventory

# Imagine that a vanquished dragon’s loot is represented as a list of strings
# like this: dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Write a function named addToInventory(inventory, addedItems), where the
# inventory parameter is a dictionary representing the player’s inventory (like
# in the previous project) and the addedItems parameter is a list like dragonLoot.

# The addToInventory() function should return a dictionary that represents the
# updated inventory. Note that the addedItems list can contain multiples of the
# same item. Your code could look something like this:


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory


def displayInventory(inv):
    total = 0
    print('Inventory:')
    for k, v in inv.items():
        total = total + v
        print(str(v) + ' ' + k)
    print('Total number of items: ' + str(total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

# The previous program (with your displayInventory() function from the
# previous project) would output the following:

# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
# Total number of items: 48

