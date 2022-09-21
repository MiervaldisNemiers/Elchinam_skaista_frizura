import random
things = ["rock", "paper", "scissors"]
computer_turn = random.choice(things)
human_turn = input("Izvēlies. rock, paper vai scissors:").lower()
print('Dators izvēlas: ' + computer_turn)
if human_turn == computer_turn:
    print("Neizšķirts")
elif human_turn == "rock" and computer_turn == "paper":
    print("Dators uzvar!")
elif human_turn == "paper" and computer_turn == "scissors":
    print("Dators uzvar!")
elif human_turn == "scissors" and computer_turn == "rock":
    print("Dators uzvar!")
else:
    print("Tu uzvarēji!")
