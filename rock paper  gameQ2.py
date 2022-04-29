import random

def win():
    print("you win!")

def lose():
    print("you lose")

while True:
    player_choise=input("what do you pic?(rock,paper,scissers):>")
    player_choise.strip()
    moves=["rock","paper","scissers"]
    random_move=random.randint(0,2)
    computer_choise=moves[random_move]
    print(computer_choise)
    if player_choise==computer_choise:
        print("draw")
    elif moves=="rock" and computer_choise=="scissers":
        win()
    elif player_choise=="paper" and computer_choise=="scissers":
        lose()
    elif player_choise=="scissers" and computer_choise=="paper":
        win()
    elif player_choise=="scissers" and computer_choise=="rock":
        lose()
    elif player_choise=="paper" and computer_choise=="rock":
        lose()
    elif player_choise=="scissers" and computer_choise=="rock":
        lose()
    again=input("do you want to play again?(y or n:>)")
    if again=="n":
        break


