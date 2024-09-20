name = "Manjeet-Yadav"
isLegalString = False
copyName = name.replace("-","");
copyName = name.replace(" ","");
copyName = name.replace("'","");
print(copyName,"After replacing the dashes, spaces & apostrophies");
if len(copyName) >0:
    if type(copyName[0].isalpha()):
        if len(copyName) == 1:
            isLegalString = True
        else:
            if copyName != copyName.upper():
                if copyName.isalnum():
                    isLegalString = True
                else:
                    isLegalString = False
            else:
                isLegalString = False
    else:
        isLegalString = False
else:
    isLegalString = False

print("Is",name,"a legal string ?",isLegalString)

# Another way
if not copyName.isalnum():
    isLegalString = False
elif len(copyName) == 1 and copyName.isalpha():
    isLegalString = True
elif len(copyName) >= 1 and copyName.upper() == copyName:
    isLegalString = True
elif len(copyName) > 1 and copyName[0].isalpha():
    isLegalString = True
else:
    isLegalString = False
print("Is",name,"a legal string ?",isLegalString)

# Another way
if not copyName.isalnum():
    isLegalString = False
elif len(copyName) == 1 and  not copyName.isalpha():
    isLegalString = False
elif len(copyName) >= 1 and copyName.upper() == copyName:
    isLegalString = False
elif len(copyName) > 1 and not copyName[0].isalpha():
    isLegalString = False
else:
    isLegalString = True
print("Is",name,"a legal string ?",isLegalString)