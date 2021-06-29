import random
while True:
    choices=["scissor","rock","paper"]
    computer=random.choice(choices)
    player=input("enter either scissor or rock or paper:").lower()
    if computer==player:
        print("computer:",computer)
        print("player:",player)
        print("tie!")
    elif player=="rock":
        if computer=="paper":
            print("computer:",computer)
            print("player:",player)
            print("you lose!")
        if computer=="scissor":
            print("computer:", computer)
            print("player:", player)
            print("you win")
    elif player=="scissor":
        if computer=="rock":
            print("computer:",computer)
            print("player:",player)
            print("you lose!")
        if computer=="paper":
            print("computer:", computer)
            print("player:", player)
            print("you win")
    elif player=="paper":
        if computer=="scissor":
            print("computer:",computer)
            print("player:",player)
            print("you lose!")
        if computer=="rock":
            print("computer:", computer)
            print("player:", player)
            print("you win")
    play_again=input("play again:(yes/no):").lower()
    if play_again !="yes":
        break
print("end game!")