"""Task 1 of Module 3."""
import pyinputplus as pyip

BREAD = {'wheat': 1.321, 'white': 2.5, 'sourdough': 40}
PROTEIN = {'chicken': 32.3, 'turkey': 55, 'ham': 1, 'tofu': 0.1}
CHEESE = {'cheddar': 5, 'Swiss': 5.5, 'mozzarella': 1000}
SAUCE = {'mayo': 300, 'mustard': 400, 'lettuce': 500, 'tomato': 600}

sandwich_ingredients = []


def sandwich_maker():
    """Provide information on ordered sandwich/es.

    Based on users input, provides information on:
    number of ordered sandwiches;
    sandwich's ingredients;
    order's price
    """
    while True:

        bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'])
        sandwich_price = BREAD[bread_type]
        sandwich_ingredients.append(bread_type)

        protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
        sandwich_price = PROTEIN[protein_type] + sandwich_price
        sandwich_ingredients.append(protein_type)

        optional_cheese = pyip.inputYesNo(
            prompt="Would you like to add cheese?\n",
            caseSensitive=False)
        if optional_cheese == "yes":
            cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
            sandwich_price = CHEESE[cheese_type] + sandwich_price
            sandwich_ingredients.append(cheese_type)

        optional_sauce = pyip.inputYesNo(
            prompt="Would you like to add sauce?\n",
            caseSensitive=False)
        if optional_sauce == "yes":
            sauce_type = pyip.inputMenu(['mayo', 'mustard',
                                         'lettuce', 'tomato'])
            sandwich_price = SAUCE[sauce_type] + sandwich_price
            sandwich_ingredients.append(sauce_type)

        number_of_sandwiches = pyip.inputInt(
            prompt="How many sandwiches would you like to buy?\n")
        sandwich_price = "{:.2f}".format(sandwich_price * number_of_sandwiches)

        print(
            "Your sandwich consists of " + ', '.join(sandwich_ingredients)
            + f". You wanted {number_of_sandwiches} sandwich(es). "
              f"That's a total of {sandwich_price} kg of gold")

        break


sandwich_maker()
