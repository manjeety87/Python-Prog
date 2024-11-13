materials = ["Wood", "Stone", "Brick", "Wood", "Glass"]
print(materials)
materials.append("Concrete")
print(materials)
print("Note that remove is case-sensitive")
print("Trying to remove 'stone'")
if "stone" in materials:
    materials.remove("stone")
print(materials)
print("Trying to remove 'Stone'")
if "Stone" in materials: 
    materials.remove("Stone")
print(materials)
#Safer removal, less opportunity for errors
elementToRemove = "Brick"
print("Trying to remove '" + elementToRemove + "'")
if elementToRemove in materials:
    materials.remove(elementToRemove)
print(materials)

elementToRemove = "Fencing"
print("Trying to remove '" + elementToRemove + "'")
if elementToRemove in materials:
    materials.remove(elementToRemove)
print(materials)

#What happens if an element occurs multiple times in the list?
print("Removing 'Wood'")
materials.remove("Wood")
print(materials)
print("Appending more Wood")
materials.append("Wood")
print(materials)
#Write some code that will remove ALL instances of the word "Wood" from the list
print("Removing all instances of Wood from the list")
#Variable for the element I want to remove
elementToRemove = "Wood"
while elementToRemove in materials:
    materials.remove(elementToRemove)
print(materials)

#What happens when you try to insert an element into a list
# at an index outside the range of the list?
newIndexA = len(materials)
materials.insert(newIndexA, "Mortar")
print(materials) #OK to add as new last element, same as append
newIndexB = len(materials) + 3
materials.insert(newIndexB, "Ceramic")
print(materials) #OK, if the index is too large it just puts it at the end

