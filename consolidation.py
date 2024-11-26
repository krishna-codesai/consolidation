# imports the random module 
import random

# Target score to win the game
target = int(input("Enter the target score to win or default to 50: ") or 50)
# Max re-rolls 
max_re_rolls = int(input("Enter the maximum re-rolls or default to 5: ") or 5)

def roll_dice():
    """ Simulates rolling 3 dice. """
    return [random.randint(1, 6) for _ in range(3)]

def tuple_out(dice):
    """ Checks if all three dice are the same, indicating the player has 'tupled out'. """
    return dice[0] == dice[1] == dice[2]

def fixed_dice(dice):
    """ Identifies indices of dice that should be fixed if two dice are the same. """
    counts = {x: dice.count(x) for x in dice}
    fixed_indices = []
    for i in range(len(dice)):
        if counts[dice[i]] == 2:
            fixed_indices.append(i)
    return fixed_indices


def re_roll_dice(dice, fixed_indices):
    """ Re-rolls only non-fixed dice """
    return[random.randint(1,6) if i not in fixed_indices else dice[i] for i in range(3)]

def get_player_choice(player_name):
    """ Validates the input for stopping or continuing the turn."""
    while True:
        choice = input(f"{player_name}, stop and keep score? (y/n): ").strip().lower()
        if choice in {"y", "n"}:
            return choice 
        else: 
            print("Invalid input. Please enter 'y' or 'n'.")

def play_turn(player_name, computer=False):
    """ Plays one turn for a player."""
    dice = roll_dice()
    roll_history = []
    print(f"{player_name} rolls: {dice}")
    
    # Check if the player tupled out
    if tuple_out(dice):
        print(f"Tuple out! {player_name} scores 0 points this turn.")
        return 0

    # Check if the player rolled a fixed dice 
    if fixed_dice(dice):
        print(f"{player_name} rolled a fixed dice! The score will be kept.")
        score = sum(dice)
        print(f"{player_name} scores {score} points this turn.")
        print(f"Roll history for this turn: {roll_history}")
        return score
    
    roll_history.append(tuple(dice))  # Record the initial roll
    fixed = fixed_dice(dice)  # Determine fixed dice
    re_roll_count = 0

    while re_roll_count < max_re_rolls: 
        # Limit the number of rerolls
        if computer:
            stop = "y" if sum(dice) >= 12 or random.choice([True,False]) else "n"
        else:
            stop = get_player_choice(player_name)
        # If the player decides to stop the game 
        if stop == "y":
            # Adds player's score
            score = sum(dice)
            print(f"{player_name} scores {score} points this turn.")
            print(f"Roll history for this turn: {roll_history}")
            return score
        else: 
            # If the player decides to re-roll
            re_roll_count += 1
            dice = re_roll_dice(dice,fixed)
            roll_history.append(tuple(dice))
            print(f"{player_name} re-rolls: {dice}")

        # Check for tuple out after re-roll
        if tuple_out(dice):
            print(f"Tuple out! {player_name} scores 0 points this turn.")
            return 0

# Game loop
scores = [0, 0]
player_names = ["Player 1", "Player 2"]
current_player = 0

while max(scores) < target:
    print(f"\n{player_names[current_player]}'s turn!")
    turn_score = play_turn(player_names[current_player])
    scores[current_player] += turn_score
    print(f"{player_names[current_player]}'s total score: {scores[current_player]}")
    current_player = 1 - current_player  # Switch players

winner = player_names[0] if scores[0] >= target else player_names[1]
print(f"\n{winner} wins with a score of {max(scores)}!")
