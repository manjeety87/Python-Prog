nums = [0,1,2,3,4,5,]
for num in nums:
    print(num)


print("Groceries list")
groceries = ["Eggs","Bacons","Bread","Cheese","Butter"]
for item in groceries:
    print(item)


print("Groceries list Reversed")
groceries = ["Eggs","Bacons","Bread","Cheese","Butter"]
for item in reversed(groceries):
    print(item)

# Access by index, the long way
groceriesIndexListA = []
indexA = 0
while indexA < len(groceries):
    groceriesIndexListA.append(indexA)
    indexA = indexA + 1
print(groceriesIndexListA)

for index in groceriesIndexListA:
    print(groceries[index])


# Generate list of indexes using
print("Using range to generate list of indexes")
for index in range(len(groceries)):
    print(str(index),groceries[index])

rangeEx1 = list(range(10,0,-1))
print(rangeEx1)