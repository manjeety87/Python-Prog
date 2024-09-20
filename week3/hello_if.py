num1 = 10
if num1 == 10:
    print("num1 is 10!!")

#what if we want to check if a value isn't the same


#we can also ask additional questions like 
# "and or "or"


min = 3
max = 10
numCheck1 = 2
numCheck2 = 10
numCheck3 = 15

print("Comparision using 'and'")
if(numCheck1 >= min and numCheck1 <= max):
    print(numCheck1, "is between",min,"and",max)
if(numCheck2 >= min and numCheck2 <= max):
    print(numCheck2, "is between",min,"and",max)
if(numCheck3 >= min and numCheck3 <= max):
    print(numCheck3, "is between",min,"and",max)

print("Comparision using 'or'")
if(numCheck1 < min or numCheck1 > max):
    print(numCheck1, "is between",min,"and",max)
if(numCheck2 < min or numCheck2 > max):
    print(numCheck2, "is between",min,"and",max)
if(numCheck3 < min or numCheck3 > max):
    print(numCheck3, "is between",min,"and",max)

#what if we have more than one relevant question ?
if num1 < 10:
    print("num1 < 10")
else:
    print("num1 >= 10")

num2 = -78
if num2 > 0:
    print(num2,"is positive")
elif num2 < 0:
    print(num2,"is negative")
elif num2 ==0 :
    print(num2,"is zero")
else:
    print(num2,"is not a number")


print("Execution completed")

# This code won't work because the order of the tests
grade = 85
print("Bad grade function for grade",grade)
if grade <50:
    print("Failed")
elif grade >= 50:
    print("D")
elif grade >= 60:
    print("C")
elif grade >= 70:
    print("B")
elif grade >= 80:
    print("A")

    
# This code does work because we the changed the order of the tests
print("Good grade function for grade",grade)
if grade <50:
    print("Failed")
elif grade >= 50:
    print("D")
elif grade >= 60:
    print("C")
elif grade >= 70:
    print("B")
elif grade >= 80:
    print("A")