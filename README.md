# woven_monopoly
Coding test

## Explanation

### dice_roll()
* This method allows for testing using randomly generated rolls.

### Player class
* Stores the data for the each player of the game.

### Game class
* Stores the data and simulates the game play
* Initialises the board, players list, and the locations of each player.
* The error handling prevents the user giving an invalid path, or duplicate names (as the locations dict requires each player have a unique name).

The main function play() simulates rounds of play until a player goes bankrupt. It then prints the final state.

The turn() function runs a turn for a player, performing dice rolls and any necessary buying or rent payments

## Extensibility
* Dice rolling uses function dice_roll() allowing to extend method for multiple rolls, different number of die sides, or rolling at advantage or disadvantage (rolling two die and selecting the higher or lower of the two results)
* The Player class could methods to simulate player behaviour, such as making choices about gameplay. The data here could be displayed to each user.
* Could extend Game class to include a save or load for the current state of Players and player locations

## Final output for each game:
### Game 1
