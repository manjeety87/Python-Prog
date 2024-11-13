
validInput = False

while not validInput:
    #Here we do some code
    userInput = input("Please enter a number: ")
    if not userInput.isnumeric():
        print(userInput, "is not a valid number.")
    else:
        number = float(userInput)
        validInput = True
#This is the bottom of the while loop

print("The user input the number", number)



