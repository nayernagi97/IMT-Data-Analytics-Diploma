import random

random_number = random.randint(1,100)
print("welcome to the number guessing game!!")

while(True):
    guess = int(input("please enter your guess:\n"))
    if guess == random_number:
        print("congratulation you guessed correctly")
        break
    else:
        hint = "higher" if random_number > guess else "lower" 
        print("let me give you a hint the number was {} than your guess".format(hint))

    if input("do you want to continue(y/n):\n").lower() == "n":
        break