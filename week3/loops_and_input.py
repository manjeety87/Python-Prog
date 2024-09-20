validInput = False

while not validInput:
    userInput = input("Please enter a number :")
    if not userInput.isnumeric():
        print(userInput,"is not a valid number")
    else:
        number = float(userInput)
        validInput = True
print("The user input the number", number)