config = {
    # key : value,
    "resolution" : "1024x768",
    "save game dir" : "c:/user/me/savegames/",
    "refresh" : 60,
    "username" : ""
}

print(config)

#Write/add/modify new elements
config["level"] = 4
print(config)
config["username"] = "kevin"
print(config)
if not "resolution" in config:
    config["resolution"] = "640x480"
print(config)
config.update({"refresh" : 120})
config.update({"password" : "p@ssword"})
print(config)

#Read elements
# [] and get() are both safe when the key exists
print(config["level"])
print(config.get("level"))
# [] and get() behave differently when the key does not exists
# [] throws an exception of type KeyError
try:
    nextLevel1 = config["next level"]
    print(nextLevel1)
except KeyError:
    print("Value not found in dictionary")
# get() returns a value of None
nextLevel2 = config.get("next level")
if nextLevel2 == None:
    print("Value not found in dictionary")
else:
    print(nextLevel2)

#iterating through the keys
print("Iterate through the keys one by one:")
for k in config.keys():
    print(k)
#keys() actually returns what we call a "view", which is a list that keeps itself up to date with any changes to the main collections.
config_keys = config.keys()
print("Number of keys: ", len(config_keys))
print(config_keys)
config["high_score"] = 1000000000
print("Number of keys: ", len(config_keys))
print(config_keys)

#Doesn't work, can't assign to a view
#config_keys[0] = "new key"
#Doesn't work, can't add new elements to a view
#config_keys.append("new key")


#There is also a view for the values, which works the same way
config_values = config.values()
for val in config_values:
    print(val)
    
#We can also look at the key-value pairs together by iterating through the items collection of the dictionary.
#Because items() is a list of key-value pairs, we can assign each element of the pair to its own variable in the loop.
for k, v in config.items():
    print(f"Key: {k} Value: {v}")
    
config_items = config.items()
print(type(config_items))
for kvp in config_items:
    print(type(kvp), kvp)

for i, kvp in enumerate(config.items()):
    print(f"Index: {i} Key: {kvp[0]} Value: {kvp[1]}")

#This won't work because i = key and kvp = value
#This is why we need to name our values carefully    
#for i, kvp in config.items():
#    print(f"Index: {i} Key: {kvp[0]} Value: {kvp[1]}")

i = 0
for k, v in config.items():
    print(f"Index: {i} Key: {k} Value: {v}")
    i = i + 1
    
#Example of using enumerate to find the index at which a match occurred    
colorList = ["red", "blue", "green", "purple"]
for i, color in enumerate(colorList):
    if (color == "green"):
        print("Green found at index", i)
        break