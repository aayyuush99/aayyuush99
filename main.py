import random

randNO = random.randint(1, 100)
userguess = None
guesses = 0

while(userguess != randNO):
    userguess = int(input("Enter the number: "))
    guesses = guesses + 1

    if userguess == randNO:
        print("++++++++++++++++++++++++++++++")
        print("Yes! You guessed it right")
        print("++++++++++++++++++++++++++++++")
    elif userguess < randNO:
        print("You guessed it Wrong")
        print("Please enter a higher value")
    elif userguess > randNO:
        print("You guessed it Wrong")
        print("Please enter a lower value")


print(f"You guessed in {guesses} times")

with open("hiscore_for_rand.txt") as f:
    data = int(f.read())

if (guesses<data):
    print("You have just broken the high score! ")
    with open("hiscore_for_rand.txt" , "w") as f:
        f.write(str(guesses))

