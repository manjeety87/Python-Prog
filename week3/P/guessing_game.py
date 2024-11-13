#A more practical example
numberToGuess = 67
numMin = 0
numMax = 100
userGuess = -1
print("Welcome to the guessing game.")
while userGuess != numberToGuess:
    userInput = input("Guess a number between " + str(numMin) + " and " + str(numMax) + ": ")
    #Add code that validates the input. If the input is an integer, put the value into userGuess
    # otherwise print an error message.
    #Add code that prints an error message if the inputted number does not lie in the range of
    # numMin to numMax inclusive
    #Add code that gives the user a hint of "higher" or "lower".
    # The hint code should only run if the user guess is in the range of numMin and numMax
    #For homework - Add a counter that keeps track of how many valid guesses it takes until you
    # guess the number. A valid guess is a number that lies between numMin and numMax, including the
    # final correct guess.
    if userInput.isnumeric():
        userGuess = int(userInput)
        if userGuess < numMin:
            print("Error, guess must be bigger than", numMin)
        elif userGuess > numMax:
            print("Error, guess must be smaller than", numMax)
        else:
            if userGuess < numberToGuess:
                print("Higher")
            elif userGuess > numberToGuess:
                print("Lower")
    else:
        print("Error, input must be a number.")
print("You win!")