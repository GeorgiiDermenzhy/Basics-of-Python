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
    bread_type = pyip.inputMenu(list(BREAD.keys()))
    sandwich_price = BREAD[bread_type]
    sandwich_ingredients.append(bread_type)

    protein_type = pyip.inputMenu(list(PROTEIN.keys()))
    sandwich_price += PROTEIN[protein_type]
    sandwich_ingredients.append(protein_type)

    optional_cheese = pyip.inputYesNo(
        prompt="Would you like to add cheese?\n",
        caseSensitive=False)
    if optional_cheese == "yes":
        cheese_type = pyip.inputMenu(list(CHEESE.keys()))
        sandwich_price += CHEESE[cheese_type]
        sandwich_ingredients.append(cheese_type)

    optional_sauce = pyip.inputYesNo(
        prompt="Would you like to add sauce?\n",
        caseSensitive=False)
    if optional_sauce == "yes":
        sauce_type = pyip.inputMenu(list(SAUCE.keys()))
        sandwich_price += SAUCE[sauce_type]
        sandwich_ingredients.append(sauce_type)

    # don't like how it looks like, but this is what
    # pylint and flake8 advised me to do:
    number_of_sandwiches = pyip.inputInt(min=1,
                                         prompt="How many sandwiches would "
                                                "you like to buy?\n")

    total_price = sandwich_price * number_of_sandwiches

    print(
        f"Your sandwich consists of {', '.join(sandwich_ingredients)}"
        f". You wanted {number_of_sandwiches} sandwich(es). "
        f"That's a total of {total_price:.3f} kg of gold")


sandwich_maker()
