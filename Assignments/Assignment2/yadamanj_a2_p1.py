# inputNumber = input("Enter the value in cents ( 0 - 500) : ")
# wrongInputTimes = 0
# # exitWhileLoop = True;

# if inputNumber.isnumeric():
#     #  then calulate
# else:
#     print("Invalid input: Please enter a valid number.")

# def validateInput(inputNumber):
#      if inputNumber >= 5:
#             terminateOrNot = input("You've entered too many invalid inputs. Do you want to continue? (y/n): ")
#             if terminateOrNot.lower() == 'n':
#                 print("Program ended.")
#                 exit()
#             return 0

# while True:
#         inputNumber = input("Enter the value in cents ( 0 - 500) : ")

#         if inputNumber.isnumeric():
#             inputNumber = int(inputNumber)
#             if 0 < inputNumber and inputNumber > 500:
#                 inputNumber
#             else:
#                 print("Invalid input: The number must be between 0 and 500 (exclusive).")
#         else:
#             print("Invalid input: Please enter a valid number.")
        
#         wrongInputTimes += 1
#         # wrongInputTimes = validateInput(wrongInputTimes)
#         if wrongInputTimes >= 5:
#             terminateOrNot = input("You've entered too many invalid inputs. Do you want to continue? (y/n): ")
#             if terminateOrNot.lower() == 'n':
#                 print("Program ended.")
#                 exit()
#             wrongInputTimes = 0  # Reset invalid attempts after prompt

# # while exitWhileLoop:
# #     inputNumber = input("Enter a number between 0 to 500 : ")

#     # if(int(inputNumber) < 0 or int(inputNumber) > 500):
#     #     wrongInputTimes = wrongInputTimes + 1
#     # if(wrongInputTimes == 4):
#     #     terminateOrNot = input("You have entered wrong input 5 times, do you want to continue (y/n) : ")
#     #     if terminateOrNot == "n" or "N":
#     #         exitWhileLoop = False
#     #     else:
#     #         wrongInputTimes = 0
#     #         continue
# # print("The number you entered is : ", inputNumber)

def terminateProgram():
    print("Ok, see you later!")
    exit()

def calculateCents(cents):
    # coins = {'Twoonies': 200, 'Loonies': 100, 'Quarters': 25, 'Dimes': 10, 'Nickels': 5, 'Pennies': 1}
    coins = ["Twoonies: 200", "Loonies: 100", "Quarters: 25", "Dimes: 10", "Nickels: 5", "Pennies: 1"]
    print(f"\nFor {cents} cents, you need:")
    for coin in coins:
        centValue = coin.split(': ')[1]
        centValue = int(centValue)
        # use floor division so that we cannot get a decimal and the rest amount can be calculated 
        numberOfCoins = cents // centValue
        cents %= centValue
        print(f"{coin}: {numberOfCoins}")
    print()


def checkToTerminate():
    terminateOrNot = input("You have entered wrong input 5 times, do you want to continue (y/n) : ")
    if terminateOrNot.lower() == "n":
        terminateProgram()
    return False
    # if wrongInputTimes == 5:
    #     terminateOrNot = input("You have entered wrong input 5 times, do you want to continue (y/n) : ")
    #     if terminateOrNot.lower() == "n":
    #         terminateProgram()
    #     else:
    #         wrongInputTimes = 0
    #         return True
    # return False

wrongInputTimes = 0
while True:
    inputNumber = input("Enter the value in cents ( 0 - 500) : ")

    if not inputNumber.isnumeric():
        wrongInputTimes += 1
        # inputNumber = input("SECOND <--> time input")
        # inputNumber = input("Enter the value in cents ( 0 - 500) : ")
        print("Input called ",wrongInputTimes ,"times")
        if wrongInputTimes == 5:
            print("Not input called % TIME",wrongInputTimes ,"times")
            checkToTerminate()

            print("::::STATEMENT CALLED AFTER TERMINATE",wrongInputTimes ,"times")
            wrongInputTimes = 0
    else:
        inputNumber = int(inputNumber)
        if inputNumber >= 0 and inputNumber <= 500:
            print("The number entered is INTEGER :::: ")
            wrongInputTimes = 0
            calculateCents(inputNumber)
            checkToTerminate()
        else:
            print("Invalid input: The number must be between 0 and 500 (exclusive).")
            wrongInputTimes += 1

        # if wrongInputTimes == 5:
        #     checkToTerminate()
            # terminateOrNot = input("You have entered wrong input 5 times, do you want to continue (y/n) : ")
            # wrongInputTimes = 0
            # if terminateOrNot.lower() == "n":
            #     terminateProgram()