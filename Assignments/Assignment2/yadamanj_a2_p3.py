listOfStrings = input("Enter a list of strings separated by commas: ").split(" ")
print("There are",len(listOfStrings),"strings in the list.")
alphabetized_flag = False

menu = ["Clear list","Print list", "Alphabetize list","Add word(s) to list","Delete word(s) from list","Remove duplicate words from list" ,"Exit program"]

def clearListOfStrings():
    clearOrNot = input("Are you sure you want to clear the list? (y/n): ")
    if clearOrNot.lower() == "y":
        listOfStrings.clear()
    else:
        print("List not cleared.")

def printListOfStrings():
    print("The list of strings is",listOfStrings)

def sortListByAlphabet():
    listOfStrings.sort()
    print("The list of strings after sorting is",listOfStrings)

def addWordToListOfStrings():
    while True:
        word = input("Enter a word to add to the list: ")
        listOfStrings.append(word)
        addMoreOrNot = input("Do you want to add more than words ? (y/n) ")
        if addMoreOrNot == "y":
            continue
        else:
            break
    print("The list of strings after adding is",listOfStrings)

def deleteWordFromListOfStrings():
    word = input("Enter a word to delete from the list: ")
    if word in listOfStrings:
        # word = word.lower()
        listOfStrings.remove(word)
    # listOfStrings.remove(word)
    print("The list of strings after deleting a word is",listOfStrings)

def removeDuplicateWordsFromListOfStrings(wordToRemove):
    listOfStrings.remove(wordToRemove)

def exitProgram():
    exitProgramOrNot = input("Are you sure you want to exit? (y/n): ")
    exitProgramOrNot = exitProgramOrNot.lower()
    if exitProgramOrNot == "y":
        exit()
    return

while True:
    print("Please choose an option:")
    for i in range(len(menu)):
        print(i+1,menu[i])
    option = (input("Enter your option: "))
    if not option.isnumeric():
        print("Invalid input. Please try again using numbers.")
        continue
    option = int(option)
    # switch:
    #     case 1:
    #         clearListOfStrings()
    #     case 2:
    #         printListOfStrings()
    #     case 3:
    #         sortListByAlphabet()
    #     case 4:
    #         addWordToListOfStrings()
    #     case 5:
    #         deleteWordFromListOfStrings()
    #     case 6:
    #         removeDuplicateWordsFromListOfStrings()
    #     case 7:
    #         exitProgram()
    if option == 1:
        clearListOfStrings()
    elif option == 2:
        printListOfStrings()
    elif option == 3:
        sortListByAlphabet()
    elif option == 4:
        addWordToListOfStrings()
    elif option == 5:
        deleteWordFromListOfStrings()
    elif option == 6:
        removeDuplicateWordsFromListOfStrings()
    elif option == 7:
        exitProgram()
    else:
        print("Invalid option. Please try again between 1 to 7.")
