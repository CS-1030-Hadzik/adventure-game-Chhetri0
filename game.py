
# Welcome message and introductions
print("Welcome to the Adventure Game!")  
print("Your journey begins here...")

#ASK for the player naame
player_name = input("What is your name, adventurer?")

#concatenate strings to create a personalized mess
print("Welcome, "+ player_name + "!Your journey begins now.")

#Use an f-string to display the same message in a more readable way
print(f"Welcome, {player_name}! Your journey begins now.")

# Describe the starting area
starting_area = """
you find yourself in a dark forest.
The sound of rustling leaves fille the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

# Ask the player for their first decision
decision = input ("Do you wish to take the path? (yes or no):").lower()

# Respond based on the player's decision
if decision == "yes":
        print (f"Brave choice, {player_name}! You step onto the path and venture fordward.")
elif decision == "no":
    print(player_name + ", you decide to wait. Perhaps courage will find you later.") # Concatenation example
else:
    print("confused, you stand still, unsure of what to do.")