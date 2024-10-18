# input = accepts a number from the user between range of 0 to 10000
# if it's valid then proceed further
# formula for factors = number % 2 == 0
#once factors are calulcated count how many factors we got
# If the number is a prime number (that is the only factors of that number are 1 and itself),
# prime number formula = number % 2 != 0
# if prime print message also
# input = if they want to see all the factors -  yes or no 

factors = []
def isPrimeNo(number):
    if number < 2:
        # print("0 and 1 are not a prime number")
        return False
    else:        
        for n in range(2, (number // 2 ) + 1):
            if (number % n) == 0:
                # print(number, "is not a prime number")
                break
            else:
                # print(number, "is a prime number")
                return True
    return False

def getFactorsOfANumber(number):
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    print(f"We have found {len(factors)} facors for number {number}.")
    if isPrimeNo(number):
                print(f"{number} is a prime number")

def showAllFactors(listOfFactors,number):
    print(f"The factors for the {number} are", listOfFactors)

def terminateProgram():
    print("Program ended. Thank you.")
    exit()

def checkForPrintingFactors():
    while True:
        showfactor = input("Do you want to see all the factors (y/n) ? :")
        showfactor = showfactor.lower()
        if showfactor.lower() == "n":
            terminateProgram()
        if showfactor.lower() in ['y', '']:
            showAllFactors(factors,factorInput)
            terminateProgram()
        print("Invalid input. Please try again using ['Y','y','N','n',''].")

while True:
    factorInput = input("Enter a number between range of 0 to 10000 : ---->")

    if not factorInput.isnumeric():
        print("Not a valid number, Please try again")
        # factorInput = input("Enter a number between range of 0 to 10000 :________ ")
    else:
        factorInput = int(factorInput)
        if factorInput >= 0 and factorInput <= 10000:
            print(type(factorInput),"FacotrInput",factorInput)
            getFactorsOfANumber(factorInput)
            checkForPrintingFactors()
            # if isPrimeNo(factorInput):
            #     print(f"{factorInput} is a prime number")
        

            # else:
            #     showfactor = input("Do you want to see all the factors (y/n) ? :")
            #     if showfactor in ['y', 'n', '']:
            #         showAllFactors(factors,factorInput)
            #     print("Invalid input. Please try again.")
            #     print("This is a factor")
        else:
            print("Invalid range it must be in between 0 and 10000.")
        