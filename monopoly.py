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


# Classes

class Player():
    """
    Class for the game players
    All players start with $16 and no properties
    """
    def __init__(self, name, money = 16, properties = []):
        self.name = name
        self.money = money
        self.properties = properties

# Game setup

names = ['Peter', 'Billy', 'Charlotte', 'Sweedal']
players = [Player(name) for name in names]
