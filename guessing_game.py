import random
import os

os.system("cls")

print("--------------------------")
print("Welcome to Guessing Game")
print("--------------------------")
print()

random_number = random.randint(1,100)


print("You have 5 attempts to guess the right number, between 0 and 100")
print()
guess = 1
win=False

def check(num):
    if num == random_number:
        return True
    return False

while guess<=5:
    try:
        a = int(input(f"Attempt {guess} -> What is your guess? "))
        print()
        if a<1 or a>100:
            print("Please enter a number between 1 and 100")
            print()
            continue
    except:
        print("Please enter a valid number")
        print()
        continue
    if check(a):
        print("You win!!!")
        print()
        win = True
        break
    else: 
        comparison = "higher than" if a > random_number else "lower than"
        print(f"Your guess is {comparison} the target number")
        print()
    guess+=1

if not win:
    print(f"You lost the game. The number was {random_number}")


print()
play = input("Do you want to play again (Y/N)? ")
print()

if play=="Y" or play == "y":
    os.system("python guessing_game.py")
else: 
    print("Bye bye, see you later!")
    print()
    
