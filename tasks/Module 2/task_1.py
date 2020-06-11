"""Task 1 and 2 of Module 2."""

from collections import defaultdict
# create CONSTANT variables for weight
LIGHT_WEIGHT_THRESHOLD = 60
HEAVY_WEIGHT_THRESHOLD = 70
MAX_INVENTORY_CAPACITY = 80

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# update dragonLoot variable changed to dragon_loot
dragon_loot = [

    'gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby',

    'rubbish', 'chewed gum', 'used tissue']


def display_inventory(inventory):
    # change header for display_inventory function
    """Check the inventory of a player and provides weight/speed dependency status
    """
    print("Inventory:")
    item_total = 0

    for item_name, item_count in inventory.items():
        # change print iteams , to use default print() separator settings
        print(item_name, item_count)
        # change item_total counter to use augmented assignment
        item_total += 1

    print("Total number of items: " + str(item_total))
    # here notify our hero if he/she is carrying too much
    if item_total >= LIGHT_WEIGHT_THRESHOLD:
        print(
            "CAUTION: Your backpack weighs a lot, "
            "your stamina runs out quicker!")
    elif item_total >= HEAVY_WEIGHT_THRESHOLD:
        print(
            "CAUTION: Your equipment is very heavy, "
            "you're moving slower than usual!")
    elif item_total >= MAX_INVENTORY_CAPACITY:
        print("CAUTION: You are overloaded, can't move!")


def add_to_inventory(inventory, added_items):
    """Add to inventory:

    - Adds new items to inventory of a player
    - Checks input items for trash
    - Provides information on skipped added iteams
    """

    skipped = {}
    # add implementation of defaultdict for skipped dict
    skipped = defaultdict(int)

    added_items_counter = 0

    # your code goes here
    trash = ['rubbish', 'chewed gum', 'used tissue']

    for item in added_items:
        if item in trash:
            skipped[item] += 1
        elif item in inventory:
            inventory[item] += 1
            added_items_counter += 1
        else:
            inventory[item] = 1
            added_items_counter += 1
    # change print for number of added items, to use f-strings
    print(f"Added {added_items_counter} items to the inventory")
    print("Skipped:")
    for item_name, item_count in skipped.items():
        print(item_name, item_count)
    print("===============")

    return inventory


stuff = add_to_inventory(stuff, dragon_loot)

display_inventory(stuff)
