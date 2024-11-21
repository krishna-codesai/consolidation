# imports the random module 
import random

# Target score to win the game
target = 100

def roll_dice():
    """ Simulates rolling 3 dice. """
    return [random.randint(1, 6) for _ in range(3)]

def tuple_out(dice):
    """ Checks if all three dice are the same, indicating the player has 'tupled out'. """
    return dice[0] == dice[1] == dice[2]

def fixed_dice(dice):
    """ Identifies 'fixed' dice if two dice are the same. """
    counts = {x: dice.count(x) for x in dice}
    fixed = []
    for i in range(len(dice)):
        if counts[dice[i]] == 2:
            fixed.append(i)
    return fixed

def play_turn(player_name, computer=False):
    """Plays one turn for a player."""
    dice = roll_dice()
    roll_history = []
    print(f"{player_name} rolls: {dice}")
    
    # Check if the player tupled out
    if tuple_out(dice):
        print(f"Tuple out! {player_name} scores 0 points this turn.")
        return 0
    
    roll_history.append(tuple(dice))  # Record the initial roll
    fixed = fixed_dice(dice)  # Determine fixed dice
    re_roll_count = 0

    while True:
        # Limit the number of rerolls
        if re_roll_count >= 5:
            print(f"Maximum re-rolls reached for {player_name}.")
            break

        if not computer:
            stop = input(f"{player_name}, stop and keep score? (y/n): ").strip().lower()
        else:
            stop = "y" if random.choice([True, False]) else "n"

        if stop == "y":
            score = sum(dice)
            print(f"{player_name} scores {score} points this turn.")
            print(f"Roll history for this turn: {roll_history}")
            return score

        # Re-roll logic
        re_roll_count += 1
        for i in range(3):
            if i not in fixed:
                dice[i] = random.randint(1, 6)
        roll_history.append(tuple(dice))  # Record the reroll
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
