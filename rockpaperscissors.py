print('Rock Paper Scissors')
import random
choice = input('What is your choice? ')
computer = random.choice(["rock", "paper", "scissors"])

print("Computer chose: " + computer)

if choice == "paper" and computer == "rock": print('You win')
elif choice == "scissors" and computer == "paper": print('You win')
elif choice == "rock" and computer == "scissors": print('You win')
elif choice == "rock" and computer == "paper": print('You lost')
elif choice == "paper" and computer == "scissors": print('You lost')
elif choice == "scissors" and computer == "rock": print('You lost')
else: print('Tie')

