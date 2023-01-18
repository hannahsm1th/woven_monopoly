# Woven Monopoly
# Hannah Smith Coding Test
# January 2023

# Imports
import random
import json


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


class Game():

    """
    Class for the game logic, simulating the players movements around the board.
    The game board is created from a given path to a JSON file.
    """

    def __init__(self, board_path, player_names):
        # Import JSON from the given path
        try:
            if type(board_path) is not str:
                raise Exception("Board path should be a string giving the path to the JSON file")
            with open(board_path, 'r') as f:
                self.board = json.load(f)
            if len(self.board) < 1:
                raise Exception("Given JSON file is empty")
        except json.decoder.JSONDecodeError:
            print("Cannot decode given JSON file")
        except FileNotFoundError:
            print("Board path should give the path to a JSON file")

        # Initialise a Player instance for each player name
        if len(player_names) != len(set(player_names)):
            raise Exception("List cannot contain duplicate names.")
        self.players = [Player(name) for name in player_names]

        # Create a dictionary to store where the players are
        self.player_locations = {}
        # Begins by placing each player at GO.
        for player in self.players:
            self.player_locations[player.name] = 0

        print("Beginning a game of Woven Monopoly for {}.".format(player_names))

    def play(self):
        """
        Simulates the game play.
        """
        for player in self.players:
            print("It's {}'s turn. They are on {}.".format(
                player.name,
                self.board[self.player_locations[player.name]]["name"]
                ))


# Game setup

names = ['Peter', 'Billy', 'Charlotte', 'Sweedal', 'Peter']

game = Game('board.json', names)

game.play()