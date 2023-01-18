# Woven Monopoly
# Hannah Smith Coding Test
# January 2023

# Imports
import random


# Methods

def dice_roll(sides = 6):
    """
    Simulates rolling a dice for a given number of sides
    Returns a number between 1 and the given number, default is 6
    """

    return random.randint(1, sides)

print(dice_roll())