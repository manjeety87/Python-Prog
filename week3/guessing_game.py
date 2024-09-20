numberToGuess = 67
numMin = 0
numMax = 100
userGuess = -1
# while userGuess != numberToGuess:


# numInput = input("Enter the number")
while userGuess != numberToGuess: 
    userInput = input("Guess a number between "+ str(numMin) + "and" + str(numMax) + ":" )
    if userInput.isnumeric():
        if int(userInput) < numberToGuess:
            print("Entered number is too low")
        if int(userInput) > numberToGuess:
            print("Entered number is too high")
        userGuess = int(userInput)
        if (userGuess > numMin and userGuess <= numMax):
            print("Number lies in between min and max")
    else:
        print("The entered number is not a integer number")

print("You win")



#OPTIMIZE For homework - Add a counter that keeps track of how manu valid guesses it takes until you guess the number. A valid guess is a number that lies between numMin and numMax, including the final correct guess.