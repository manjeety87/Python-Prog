#For loops are great for iterating over some range of things
print("Numbers from 0 to 5")
for num in [0, 1, 2, 3, 4, 5]:
    print(num)

print("Numbers from 0 to 5 again")
nums = [0, 1, 2, 3, 4, 5]
for num in nums:
    print(num)

print("Grocery list")
groceries = ["Eggs", "Bacon", "Bacon", "Bread", "Cheese"]
for items in groceries:
    print(items)

print("Grocery List Backwards revisited")
for items in reversed(groceries):
    print(items)

#Access by index, the long way
print("Generate a list of all the indexes of a list")
groceriesIndexListA = []
indexA = 0
while indexA < len(groceries):
    groceriesIndexListA.append(indexA)
    indexA = indexA + 1
print(groceriesIndexListA)

for index in groceriesIndexListA:
    print(groceries[index])

#Generate list of indexes (the fast way)
print("Using range to generate list of indexes")
for index in range(1, len(groceries)-1, 2):
    print(str(index), groceries[index])

rangeEx1 = list(range(10,0,-1))
print(rangeEx1)
