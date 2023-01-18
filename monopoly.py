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

    def __init__(self, name, money = 16):
        self.name = name
        self.money = money
        self.properties = []


class Game():

    """
    Class for the game logic, simulating the players movements around the board.
    The game board is created from a given path to a JSON file.
    """

    def __init__(self, board_path, player_names, rolls_path):
        # Import board JSON from the given path
        self.board = self.import_JSON(board_path)

        # Initialise a Player instance for each player name
        if len(player_names) != len(set(player_names)):
            raise Exception("List cannot contain duplicate names.")
        self.players = [Player(name) for name in player_names]

        # Create a dictionary to store where the players are
        self.player_locations = {}
        # Begins by placing each player at GO.
        for player in self.players:
            self.player_locations[player.name] = 0

        # Import rolls JSON from the given path
        self.rolls = self.import_JSON(rolls_path)

        print("Beginning a game of Woven Monopoly for {}.".format(player_names))


    def import_JSON(self, path):
        """
        Imports a JSON file, checking if the path is valid and the file isn't empty.
        Returns the JSON as a variable.
        """
        try:
            if type(path) is not str:
                raise Exception("Path should be a string giving the path to the JSON file")
            with open(path, 'r') as f:
                var = json.load(f)
            if len(var) < 1:
                raise Exception("Given JSON file is empty")
        except json.decoder.JSONDecodeError:
            print("Cannot decode given JSON file")
        except FileNotFoundError:
            print("Path should give the path to a JSON file")

        return var


    def play(self):
        """
        Simulates the game play.
        """
        bankrupt_player = False

        while not bankrupt_player:
            for player in self.players:
                print("{}'s turn. They are on {}.".format(
                    player.name,
                    self.board[self.player_locations[player.name]]["name"]
                    ))
                self.turn(player)
                if player.money <= 0:
                    bankrupt_player = True
                    print("{} has gone bankrupt!".format(player.name))
                    break

            # print status of each player at the end of each round of play
            print("=" * 20)
            for player in self.players:
                print("{} now has ${} and {} propert{}.".format(
                player.name,
                player.money,
                len(player.properties),
                "y" if len(player.properties) == 1 else "ies"
            ))
            print()

        winners = self.check_winner()

        print("The winner{} {}: {}!".format(
            "" if len(winners[0]) == 1 else "s",
            "is" if len(winners[0]) == 1 else "are",
            winners[1]
        ))

        for player in self.players:
            print("{} ends on {}".format(
                player.name,
                self.board[self.player_locations[player.name]]["name"]
            ))

    def check_set(self, colour):
        """
        Iterates over the properties and determines if the given color of properties all have the same owner.
        Returns a bool.
        """

        set_owners = []

        for space in self.board:
            if space["type"] == "property":
                if space["colour"] == colour:
                    if 'owner' not in space.keys():
                        return False
                    else:
                        set_owners.append(space["owner"])

        return len(set(set_owners)) == 1


    def check_winner(self):
        """
        Determines the player with the current highest amount of money.
        Returns the winning player(s) and their name(s) as a string.
        """
        current_winner = [Player("Dummy", money=0)]

        for player in self.players:
            if player.money > current_winner[0].money:
                current_winner = [player]
            elif player.money == current_winner[0].money:
                current_winner.append(player)

        winner_string = current_winner[0].name
        if len(current_winner) > 1:
            for i in range(1, len(current_winner)):
                winner_string += ", "
                winner_string += current_winner[i].name

        return current_winner, winner_string


    def turn(self, player):
        """
        Simulates a turn for the given player.
        """

        # Rolls the dice
        move = dice_roll(6)

        # Moves the player to the new location
        current_location = (self.player_locations[player.name] + move) % len(self.board)
        self.player_locations[player.name] = current_location

        print("{} has landed on {}.".format(
            player.name,
            self.board[self.player_locations[player.name]]["name"]
        ))

        if self.board[current_location]["type"] == 'go':
            player.money += 1
            print("Collecting GO money...")
        elif self.board[current_location]["type"] == 'property':
            # If property is unowned, buy it
            if 'owner' not in self.board[current_location].keys():
                if player.money >= self.board[current_location]["price"]:
                    self.board[current_location]["owner"] = player
                    player.money -= self.board[current_location]["price"]
                    player.properties.append(self.board[current_location])
                    print("{} buys {} for ${}".format(
                        player.name,
                        self.board[current_location]["name"],
                        self.board[current_location]["price"]
                    ))
            elif 'owner' in self.board[current_location].keys() and self.board[current_location]["owner"] != player:
                current_owner = self.board[current_location]["owner"]
                rent = self.board[current_location]["price"]
                if self.check_set(self.board[current_location]["colour"]):
                    rent = rent * 2
                if player.money >= rent:
                    player.money -= rent
                    current_owner.money += rent
                    print("{} pays ${} rent to {}".format(player.name, rent, current_owner.name))
                elif player.money < rent:
                    current_owner.money += player.money
                    player.money = 0
                    print("{} can't pay the required ${} rent to {}!".format(player.name, rent, current_owner.name))
        else:
            raise Exception("Board tile type not valid.")


# Game setup

names = ['Peter', 'Billy', 'Charlotte', 'Sweedal']

game = Game('board.json', names, 'rolls_1.json')

game.play()