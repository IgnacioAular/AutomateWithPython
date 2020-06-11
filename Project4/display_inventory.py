
# Developer: Ignacio Aular
# ignacio345@gmail.com
# Tue Jun 5, 12:36 AM


# You are creating a fantasy video game. The data structure to model the
# player's inventory will be a dictionary where the keys are string values
# describing the item in the inventory and the value is an integer value detail-
# ing how many of that item the player has. For example, the dictionary value
# {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
# player has 1 rope, 6 torches, 42 gold coins, and so on.
# Write a function named displayInventory() that would take any possible
# "inventory" and display it like the following:

# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

# Hint: You can use a for loop to loop through all the keys in a dictionary.

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inv):
    total = 0
    print('Inventory:')
    for k, v in inv.items():
        total = total + v
        print(str(v) + ' ' + k)
    print('Total number of items: ' + str(total))
    
displayInventory(stuff)


