import random

target = 100  # Target score to win the game

def roll_dice():
    """Simulates rolling 3 dice."""
    return [random.randint(1, 6) for _ in range(3)]

def tuple_out(dice):
    """Checks if all three dice are the same, indicating the player has 'tupled out'."""
    return len(set(dice)) == 1

def fixed_dice(dice):
    """Identifies 'fixed' dice if two dice are the same."""
    # Count how many times each value appears in the dice
    counts = {x: dice.count(x) for x in dice}
    # Fixed dice are those values that appear exactly twice
    fixed = [i for i, x in enumerate(dice) if counts[x] == 2]
    return fixed

def play_turn(player_name, computer=False):
    """Plays one turn for a player."""
    dice = roll_dice()
    roll_history = []  # To track the history of rolls for this turn
    print(f"{player_name} rolls: {dice}")
    
    # Check if the player tupled out
    if tuple_out(dice):
        print(f"Tuple out! {player_name} scores 0 points this turn.")
        return 0
    
    roll_history.append(tuple(dice))  # Append the original roll as a tuple
    
    # Determine fixed dice
    fixed = fixed_dice(dice)
    
    while True:
        # Re-roll non-fixed dice
        for i in range(3):
            if i not in fixed:
                dice[i] = random.randint(1, 6)
        roll_history.append(tuple(dice))  # Append the new roll
        
        print(f"{player_name} re-rolls: {dice}")
        
        # Check for tuple out after re-roll
        if tuple_out(dice):
            print(f"Tuple out! {player_name} scores 0 points this turn.")
            return 0
        
        # For simplicity, ask the user to stop or continue
        if not computer:
            stop = input(f"{player_name}, stop and keep score? (y/n): ").strip().lower()
        else:
            stop = "y" if random.choice([True, False]) else "n"  # Simulate computer decision
            
        if stop == "y":
            score = sum(dice)
            print(f"{player_name} scores {score} points this turn.")
            print(f"Roll history for this turn: {roll_history}")
            return score

# Game loop
scores = [0, 0]  # Scores for two players
player_names = ["Player 1", "Player 2"]
current_player = 0

while max(scores) < target:
    print(f"\n{player_names[current_player]}'s turn!")
    turn_score = play_turn(player_names[current_player])
    scores[current_player] += turn_score
    print(f"{player_names[current_player]}'s total score: {scores[current_player]}")
    current_player = 1 - current_player  # Switch players

# Announce the winner
winner = player_names[0] if scores[0] >= target else player_names[1]
print(f"\n{winner} wins with a score of {max(scores)}!")
