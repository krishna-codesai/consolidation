# imports the random module 
import random

# Target score to win the game
target = 100  

def roll_dice():
    """ Simulates rolling 3 dice. """
    # Using the random module, this function returns a random number between 1 and 6 for 3 dice 
    return [random.randint(1, 6) for _ in range(3)]

def tuple_out(dice):
    """ Checks if all three dice are the same, indicating the player has 'tupled out'. """
    # If all numbers if the set have the same value, the length of the set will be equal to one 
    # Checks if the number of values is set to one 
    # This condition will only be true if all dice have the same value
    return len(set(dice)) == 1

def fixed_dice(dice):
    """ Identifies 'fixed' dice if two dice are the same. """
    # Count how many times each value appears in the dice
    counts = {x: dice.count(x) for x in dice}
    # Fixed dice are those values that appear exactly twice
    # Initialize list for fixed dice
    fixed= []
    # Iterated over the indices of the fixed list
    for i in range (len(dice)): 
        # Checking if the value at index i appears exactly twice 
        if counts[dice[i]] == 2:
            # Added index 'i' to the fixed list 
            fixed.append(i)
            # returns updated list 
            return fixed
            

def play_turn(player_name, computer=False):
    """Plays one turn for a player."""
    dice = roll_dice()
    # To track the history of rolls for this turn 
    roll_history = [] 
    print(f"{player_name} rolls: {dice}")
    
    # Check if the player tupled out
    if tuple_out(dice):
        # Prints a message to let the player know that they tupled out. 
        print(f"Tuple out! {player_name} scores 0 points this turn.")
        # returns their new score 
        return 0
   # Append the rolls as a tuple to roll_history list as a tuple 
    roll_history.append(tuple(dice))  
    
    # Determine fixed dice
    fixed = fixed_dice(dice)

    # Loop will continue until return statement occurs 
    while True:
        # Loop iterates through all 3 indices (0,1,2)
        # If die index(i) is not in the fixed list, it is re-rolled and assigned a new value 
        for i in range(3):
            if i not in fixed:
                dice[i] = random.randint(1, 6)
                # Append the new roll to roll_history list as a tuple 
        roll_history.append(tuple(dice)) 
        # prints new values if dice is re-rolled 
        print(f"{player_name} re-rolls: {dice}")
        
        # Check for tuple out after re-roll
        if tuple_out(dice):
            print(f"Tuple out! {player_name} scores 0 points this turn.")
            return 0
        
       # Allows user to choose whether to continue or not 
        # If the player is not a computer: 
        if not computer:
            # Stops game and gives the player the option to stop and keep the score (y) or keep going (n)
            stop = input(f"{player_name}, stop and keep score? (y/n): ").strip().lower()
            # If the player is a computer:
        else:
            # Randomly chooses yes or no 
            stop = "y" if random.choice([True, False]) else "n"
        # If player chooses "y" stops the game and shows the player their score and roll history. 
        if stop == "y":
            score = sum(dice)
            print(f"{player_name} scores {score} points this turn.")
            print(f"Roll history for this turn: {roll_history}")
            return score

# Game loop
# Initializing list to score player scores  
scores = [0, 0] 
# List of player names, which correspond to a list of scores
player_names = ["Player 1", "Player 2"]
# Variable to keep track of each player's turn. 
current_player = 0

# Loop that continues until one of the players has reached or exceeded the target score of 100
while max(scores) < target:
    # Prints which players turn it is 
    print(f"\n{player_names[current_player]}'s turn!")
    # Calls the play_turn function for the current player and stores their score in the turn_score variable 
    turn_score = play_turn(player_names[current_player])
    # Adds the points earned during a player's turn to their score which is stored in the scores list 
    scores[current_player] += turn_score
    # Prints the current player's total score 
    print(f"{player_names[current_player]}'s total score: {scores[current_player]}")
    # Switches players 
    current_player = 1 - current_player  

# Creating a variable that identifies the winner if their total score is greater than or equal to the target score
winner = player_names[0] if scores[0] >= target else player_names[1]
# Announces the winner and their total score 
print(f"\n{winner} wins with a score of {max(scores)}!")
