from math import trunc
import random

print("Let's play rock paper scissors\n")
print("---------------Start---------------\n")
options = ("rock", "paper", "scissors")
playing = True

while playing:
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Enter your choice: ")

    print(f"Computer: {computer}\nPlayer: {player}")

    if computer == player:
        print("It's a tie!")
    elif (computer == "rock" and player == "paper") or \
         (computer == "paper" and player == "scissors") or \
         (computer == "scissors" and player == "rock"):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "yes":
        playing = False

print("\n------Thanks for playing!------")
