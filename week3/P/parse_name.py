name = "Kevin11"
print(name)
isLegalString = False
testString = name
testString = testString.replace("-", "")
testString = testString.replace(" ", "")
testString = testString.replace("'", "")
print(name, "after replacing characters '- ", testString)
if len(testString) > 0:
    #We need to keep processing
    if testString[0].isalpha():
        #We need to keep processing
        if len(testString) == 1:
            isLegalString = True
        else:
            #We need to keep processing
            if testString != testString.upper():
                #We need to keep processing
                if testString.isalnum():
                    isLegalString= True
                else:
                    isLegalString = False
            else:
                isLegalString = False
    else:
        isLegalString = False
else:
    isLegalString = False

print("Is", name, "a legal string?", isLegalString)

#Another way
if not testString.isalnum():
    isLegalString = False
elif len(testString) == 1 and testString.isalpha():
    isLegalString = True
elif len(testString) > 1 and (testString.upper() == testString):
    isLegalString = False
elif len(testString) > 1 and testString[0].isalpha():
    isLegalString = True
print("Is", name, "a legal string?", isLegalString)

#Can we tidy this up so that all the tests are either for a valid
# or invalid name?
if not testString.isalnum():
    isLegalString = False
elif len(testString) == 1 and not testString.isalpha():
    isLegalString = False
elif len(testString) > 1 and (testString.upper() == testString):
    isLegalString = False
elif len(testString) > 1 and not testString[0].isalpha():
    isLegalString = False
else:
    isLegalString = True
print("Is", name, "a legal string?", isLegalString)