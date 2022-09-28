import random
things = ["rock", "paper", "scissors"]
computer_turn = random.choice(things)
human_turn = input("Ievadi savu lietu: ").lower()
print("Computer chooses: " + computer_turn)
if human_turn == computer_turn:
    print("Tie")
elif computer_turn == "rock" and human_turn == "paper":
    print("Human wins")
elif computer_turn == "paper" and human_turn == "scissors":
    print("Human wins")
elif computer_turn == "scissors" and human_turn == "rock":
    print("Human wins")
else:
    print("Computer wins")
    
