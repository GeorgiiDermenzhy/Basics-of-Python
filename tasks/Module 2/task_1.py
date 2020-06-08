"""Task 1 and 2 of Module 2."""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = [

    'gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby',

    'rubbish', 'chewed gum', 'used tissue']


def display_inventory(inventory):
    """Display inventory.

    Check the inventory of a player and provides weight/speed dependency status
    """
    print("Inventory:")
    item_total = 0

    for item_name, item_count in inventory.items():
        print(item_name + " " + str(item_count))
        item_total = item_total + item_count

    print("Total number of items: " + str(item_total))
    # here notify our hero if he/she is carrying too much
    if 60 >= item_total <= 69:
        print(
            "CAUTION: Your backpack weighs a lot, "
            "your stamina runs out quicker!")
    elif 70 >= item_total <= 79:
        print(
            "CAUTION: Your equipment is very heavy, "
            "you're moving slower than usual!")
    elif item_total > 80:
        print("CAUTION: You are overloaded, can't move!")


def add_to_inventory(inventory, added_items):
    """Add to inventory.

    - Add new items to inventory of a player
    - Checks input items for trash
    - Provides information on skipped added iteams
    """
    print("Inventory:")

    skipped = {}

    added_items_counter = 0

    # your code goes here
    trash = ['rubbish', 'chewed gum', 'used tissue']

    for item in added_items:
        if item in trash:
            if item in skipped:
                skipped[item] = skipped[item] + 1
            else:
                skipped[item] = 1
        elif item in inventory:
            inventory[item] = inventory[item] + 1
            added_items_counter += 1
        else:
            inventory[item] = 1
            added_items_counter += 1

    print("Added", added_items_counter, "items to the inventory")
    print("Skipped:")
    for item_name, item_count in skipped.items():
        print(item_name + " " + str(item_count))
    print("===============")
    return inventory


stuff = add_to_inventory(stuff, dragonLoot)

display_inventory(stuff)
