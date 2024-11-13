#Start with the simplest, the if statement.
num1 = 11
if num1 == 10:
    print("Num 1 is 10!!")
    print("This should only print if num1 == 10")

#What if we want to check if a value isn't the same?
num2 = 14
if num1 != num2:
    print("num1 isn't the same as num2")

#We also have less than, greater than, 
# less than or equal to, and greater than or equal to
if num1 < num2:
    #less
    print("num1 < num2 is true")
if num1 > num2:
    #greater
    print("num1 > num2 is true")
if num1 <= num2:
    #less or equal
    print("num1 <= num2 is true")
if num1 >= num2:
    #greater or equal
    print("num1 >= num2 is true")

#We can also ask additional questions like
# "and" and "or"
# Is this number between 3 and 10? becomes
#  is this number greater than or equal to 3?
# AND
#  is this number less than or equal to 10?
min = 3
max = 10
numCheck_1 = 2
numCheck_2 = 5
numCheck_3 = 15
print("Comparison using 'and'")
if numCheck_1 >= min and numCheck_1 <= max:
    print(numCheck_1, "is between", min, "and", max)
if numCheck_2 >= min and numCheck_2 <= max:
    print(numCheck_2, "is between", min, "and", max)
if numCheck_3 >= min and numCheck_3 <= max:
    print(numCheck_3, "is between", min, "and", max)

print("Comparison using 'or'")
if not (numCheck_1 < min or numCheck_1 > max):
    print(numCheck_1, "is between", min, "and", max)
if not(numCheck_2 < min or numCheck_2 > max):
    print(numCheck_2, "is between", min, "and", max)
if not(numCheck_3 < min or numCheck_3 > max):
    print(numCheck_3, "is between", min, "and", max)

#What if we have more than one relevant question?
if num1 < 10:
    print("num1 < 10")
else:
    print("num1 >= 10")

num2 = -78
if num2 > 0:
    print(num2, "is positive!")
elif num2 < 0:
    print(num2, "is negative")
elif num2 == 0:
    print(num2, "is zero")
else:
    print(num2, "isn't positive, negative, or zero??")

grade = 70
#This code won't work because of the 
# order of the tests
print("Bad grade function for grade", grade)
if grade < 50:
    print("Failed")
elif grade >= 50:
    print("D")
elif grade >= 60:
    print("C")
elif grade >= 70:
    print("B")
elif grade >= 80:
    print("A")
#This code does work because we changed the 
# tests
print("Good grade function for grade", grade)
if grade < 50:
    print("Failed")
elif grade < 60:
    print("D")
elif grade < 70:
    print("C")
elif grade < 80:
    print("B")
elif grade >= 90:
    print("A")
print("Program is done.")