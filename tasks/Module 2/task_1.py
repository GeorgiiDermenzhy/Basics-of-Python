"""Task 1 and 2 of Module 2."""

from collections import defaultdict

LIGHT_WEIGHT_THRESHOLD = 60
HEAVY_WEIGHT_THRESHOLD = 70
MAX_INVENTORY_CAPACITY = 80
UNWANTED_ITEMS = ['rubbish', 'chewed gum', 'used tissue']

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragon_loot = [
    'gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby',
    'rubbish', 'chewed gum', 'used tissue']


def display_inventory(inventory):
    """Check the inventory and provides weight/speed dependency status."""
    item_total = 0

    print("Inventory:")

    for item_name, item_count in inventory.items():

        print(item_name, item_count)

        item_total += 1

    print("Total number of items: " + str(item_total))

    if item_total >= MAX_INVENTORY_CAPACITY:
        print("CAUTION: You are overloaded, can't move!")
    elif item_total >= HEAVY_WEIGHT_THRESHOLD:
        print(
            "CAUTION: Your equipment is very heavy, "
            "you're moving slower than usual!")
    elif item_total >= LIGHT_WEIGHT_THRESHOLD:
        print(
            "CAUTION: Your backpack weighs a lot, "
            "your stamina runs out quicker!")


def add_to_inventory(inventory, added_items):
    """Add to inventory.

    - Adds new items to inventory of a player
    - Checks input items for unwanted_items
    - Provides information on skipped added iteams
    """
    skipped = {}

    skipped = defaultdict(int)

    added_items_counter = 0

    for item in added_items:
        if item in UNWANTED_ITEMS:
            skipped[item] += 1
        elif item in inventory:
            inventory[item] += 1
            added_items_counter += 1
        else:
            inventory[item] = 1
            added_items_counter += 1

    print(f"Added {added_items_counter} items to the inventory")

    print("Skipped:")

    for item_name, item_count in skipped.items():
        print(item_name, item_count)
    print("===============")

    return inventory


stuff = add_to_inventory(stuff, dragon_loot)

display_inventory(stuff)
