userName= input("Enter your namme: ")
surname= input("YOUR SURNAME: ")
id=input("Enter your school id: ")
# print("Hello",userName,surname,id)
def userDetails(name,lastName,schoolId):
    print("Your name is :", name)
    # if(name == "Manjeet"):
    #     return
    print("Your lastname is : ",lastName)
    return name,lastName

    #return name,lastName,

test = userDetails(userName,surname,id)
print(test)