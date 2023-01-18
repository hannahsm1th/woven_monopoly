# woven_monopoly
Coding test

## Explanation

This code can be executed by running the monopoly.py file, which will run a game for each of the given rolls JSON files.

The expected output is given below, which can be used for testing. The game can also be set to verbose mode to view more information about the gameplay details in each turn.

### dice_roll()
* This method allows for testing using randomly generated rolls.

### Player class
* Stores the data for the each player of the game.

### Game class
* Stores the data for the game and simulates the game play
* Game data: the board, players list, and the locations of each player.
* The error handling for JSON imports is done with a helper class, ```import_JSON()```, which prevents the user giving an invalid path, or duplicate names (as the locations dict requires each player have a unique name).
* The main function play() simulates rounds of play until a player goes bankrupt. It then prints the final state using a ```check_winner()``` helper.
* The turn() function runs a turn for a player, performing dice rolls and any necessary buying or rent payments.
* Rental payments use ```check_set()``` to determine if a colour is all owned by one person or not.

## Extensibility
* Dice rolling uses function dice_roll() allowing to extend method for multiple rolls, different number of die sides, or rolling at advantage or disadvantage (rolling two die and selecting the higher or lower of the two results)
* The Player class could methods to simulate player behaviour, such as making choices about gameplay. The data here could be displayed to each user.
* Could extend Game class to include a save or load for the current state of Players and player locations

## Final output for each game:
### Game 1
```
====================
Peter now has $36 and 5 properties.
Billy now has $13 and 2 properties.
Charlotte now has $0 and 0 properties.
Sweedal now has $1 and 0 properties.

=========================
The winner is: Peter!

Peter ends on Massizim
Billy ends on GO
Charlotte ends on Gami Chicken
Sweedal ends on Gami Chicken
=========================
```

### Game 2
```
Sweedal has gone bankrupt!
====================
Peter now has $3 and 1 property.
Billy now has $19 and 4 properties.
Charlotte now has $27 and 2 properties.
Sweedal now has $0 and 1 property.

=========================
The winner is: Charlotte!

Peter ends on Lanzhou Beef Noodle
Billy ends on Fast Kebabs
Charlotte ends on GO
Sweedal ends on Massizim
=========================
```