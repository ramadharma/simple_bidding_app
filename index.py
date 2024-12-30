import art
import os

# Function to delete the screen
def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

print(art.hammer)
print("Welcome to Bidding App")

# Create an empty dictionary to collect the data
bid_memory = {}

# Looping the program
play = True
while play:

    # Input the value and key
    name = input("What is your name? ").lower()
    bid = int(input("How much do you bid? "))

    # Input data to empty dictionary
    bid_memory[name] = bid

    # Ask if there are more people to bid
    play_again = input("Is there anyone else to bid again [Yes/ No]?: ").lower()

    if play_again in ["yes", "y"]:
        clear_screen()  # Clear the screen if they want to continue
    else:
        play = False

# Determine the winner
if bid_memory:  # Check if there are any bids
    winner = max(bid_memory, key=bid_memory.get)  # Get the name of the highest bidder
    winning_bid = bid_memory[winner]  # Get the winning bid amount
    print(f"The winner is {winner} with a bid of ${winning_bid}.")
else:
    print("No bids were placed.")

