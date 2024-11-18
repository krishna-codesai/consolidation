import random

def roll_dice():
  """ Simulates rolling 3 dice. """
  return [random.randint(1, 6) for _in range(3)]

def tuple_out(dice):
  """ Check if all three dice are the same 
      or if the play has "tupled out." """
  return len(set(dice)) == 1 

def fixed_dice(dice):
""" Identifies "fixed dice" or if two dice are the same. """
# x is the dice value 
# counts how many times "x" appears in the list "dice" which is calculated using dice.count(x)
counts = {x: dice.count(x) for x in dice}
fixed = [x for x in counts if counts[x] == 2]
return fixed 

def play_turn(player_name, computer=False):
  """ Plays one turn for a player."""
  dice = roll_dice()
  # Initializes empty list to store rolls. 
  roll_history = []
  print(f"{player_name} rolls: {dice}")
   # message if the player has "tupled out"
  if tuple_out(dice):
    return 0 

fixed = fix_dice(dice)
# append the original roll as a tuple 
roll_history.append(tuple(dice))
