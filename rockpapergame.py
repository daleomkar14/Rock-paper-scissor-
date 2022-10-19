import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == 'q':
        flag='q'
        break
    print("you chose",user_input)
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("computer picked", computer_pick +".")

    if user_input == 'rock' and computer_pick == 'scissors':
        print("You won!")
        user_wins += 1
        continue
    
    elif user_input == computer_pick:
        print("Its tie")
        continue

    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won!")
        user_wins += 1 
        continue

    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You won!")
        user_wins += 1
        continue

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer wins", computer_wins,"times.")
print("Good buy!")