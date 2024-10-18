# def getNumberFromUser(message):
#     if message.isNumeric():
#         print(message)
#         return True
# while True:
#     userInput = input("Please enter a number :")
#     userInput = int(userInput)
#     if getNumberFromUser(userInput):
#         break
def getNumberFromUser(message):
    while True:
        userInput = input(message)
        if userInput.isnumeric():
            break
    print(userInput)
    return userInput

# number = getNumberFromUser("Please enter a number :")
# print(number)

def getNumberBetweenRange(min,max):
    if(min > max):
        min,max = max,min
    value = int(getNumberFromUser("Please input a number between" +" " + str(min) +" " + "and" +" " + str(max) + " : "))
    while (value >= min and value <= max):
        value= getNumberFromUser("Please input a number between" + str(min) + str(max) + " : ")
    return value    
number = getNumberBetweenRange(0,100) 
print("Number is : ",number)
