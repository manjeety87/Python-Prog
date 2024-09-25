#Assignment 2 not complete yet
numbers = []
breakCode = True

def checkFloat(s):
    try:
        s == "done" or float(s)
        return True
    except ValueError:
        print("Error: Invalid input. Please enter a valid floating point number or 'done'.")
        return False

while breakCode:
    n = input("Enter any numbers and type 'done' when finished : ")
    if not checkFloat(n):
        print("CHECK FLOAT")
        continue
    if n  != "done":
        n = float(n)
        if len(numbers) == 0:
            smallest = n
            largest = n
        elif n < smallest:
            print("Before Smallest",n,smallest)
            smallest = n
            print("After Smallest",n,smallest)
        else:
            largest = n
            print("Largest",n,largest)
        # if n >= smallest:
        #     print("Smallest",n,smallest)
        #     if smallest > largest:
        #         largest = n
        #         print("Largest",n,largest)
        # else:
        #     smallest = n
        #     print("In ELSE statment",n,smallest,largest)

        numbers.append(n)
    else:
        breakCode = False
        print("Numbers stored",numbers)
        print("This is the smallest number",smallest,"Largest number",largest)
        break

# name = input("Enter any numbers and type 'done' when finished")
# names = []
# while name >= 1:
#     names.append(name)
#     if name.len() <1:
#         break
# print("Names",names)
