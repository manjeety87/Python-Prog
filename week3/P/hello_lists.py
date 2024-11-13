groceries = ["Eggs", "Bacon", "Bacon", "Bread", "Cheese"]
print(groceries)
#print(groceries[1:3])
#print(groceries[-1:])
#print(groceries[-1:-5])
#print(groceries[-5:-1])
#print(groceries[-5:])
#Print the contents of the list backwards (start with "Cheese"
# and end with "Eggs")
#Let's try doing this with multiple variables
indexA = 0
indexB = 4
while indexA < len(groceries):
    print(groceries[indexB])
    indexA = indexA + 1
    indexB = indexB - 1
print("All done")

indexC = len(groceries) - 1
while indexC >= 0:
    print(groceries[indexC])
    indexC = indexC -1
print("All done 2")

indexD = -1
while indexD >= -len(groceries):
    print(groceries[indexD])
    indexD = indexD - 1
print("All done 3")

#This has a logic error
#indexE = 4
#while indexE < len(groceries):
#    print(groceries[indexE])
#    indexE = indexE - 1
#print("All done 4???")

#Another logic error
indexF = 4
while indexF > len(groceries):
    print(groceries[indexF])
    indexF = indexF - 1
print("All done 5??")

#Another logic error
indexG = 0
#Classic off by one error
#while indexG <= len(groceries): #Wrong
while indexG < len(groceries):   #Right
    print(indexG)
    print(groceries[indexG])
    indexG = indexG + 1
print("All done 6")

#Another classic off by one error
#indexH = len(groceries)        #Wrong
indexH = len(groceries) - 1     #Right
#while indexH > 0: #Wrong
while indexH >= 0: #Right
    print(indexH)
    print(groceries[indexH])
    indexH = indexH - 1
print("All done 7")

groceries.reverse()
print(groceries)
print("That was so much easier!")
groceries.reverse()
print(groceries)
groceries2 = groceries
groceries2.reverse()
print("Groceries: ")
print(groceries)
print("Groceries 2:")
print(groceries2)
