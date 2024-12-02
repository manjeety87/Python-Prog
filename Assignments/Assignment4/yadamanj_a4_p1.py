import json
import os

class ContactInfo:
    def __init__(self,contactType, contactValue):
        self.__contactType = contactType
        self.contactValue = contactValue

    def getContactType(self):
        return self.__contactType;
    
    
    def serialize(self):
        return {
            "contactType":self.__contactType,
            "contactValue":self.contactValue
        }
    def __str__(self):
        return f"{self.__contactType}: {self.contactValue}"
    
    def deSerialize(data:dict):
        return ContactInfo(data["contactType"],data["contactValue"])
    
class Person:
    def __init__(self, firstName, lastName):
    # def __init__(self, firstName, lastName,contacts,numContacts,primaryContactIndex,primaryAddressIndex):
        self.firstName = firstName
        self.lastName = lastName
        self.contacts = []
        self.numContacts = 0
        self.primaryContactIndex = None
        self.primaryAddressIndex = None

    def addContact(self, contact:ContactInfo, setPrimary:bool=False):
        print("Contact Type",contact.getContactType())
        if len(self.contacts) == 0:          #if no contacts set default contact as primary
            self.primaryContactIndex = 0
        self.contacts.append(contact)
        self.numContacts += 1
        print("NO SELF PRIMARY CONTACT",not self.primaryContactIndex)
        
        # if not self.primaryContactIndex:
        #     self.primaryContactIndex = self.numContacts - 1
        # print("PRIMARY INDEX",self.primaryContactIndex)

        if setPrimary:
            print("INDEX",len(self.contacts) - 1)
            if contact.getContactType().lower() != "address":  # Check if it's not an address
                self.setPrimaryContact(self.numContacts - 1)
            else:
                self.setPrimaryAddress(self.numContacts - 1)
            # self.primaryContactIndex = self.numContacts - 1
        # else:
    def getContact(self, index:int):
        if index >= 0 and index <= len(self.contacts):
            return self.contacts[index]
        return ("Invalid index number")
    
    def setPrimaryContact(self, index:int):
        if index >= 0 and index < len(self.contacts):
            if self.contacts[index].getContactType().lower() != "address":
                self.primaryContactIndex = index
        else:
            print("Invalid index number")

    def setPrimaryAddress(self,index:int):
        print("INDEX ------------> ",index,index >= 0,index <= len(self.contacts))
        if index >= 0 and index < len(self.contacts):
            if self.contacts[index].getContactType().lower() != "phone":
                self.primaryAddressIndex = index
        else:
            print("Invalid index number")

    def serialize(self):
        return {
            "firstName":self.firstName,
            "lastName":self.lastName,
            "contacts":[contact.serialize() for contact in self.contacts],
            "numContacts":len(self.contacts),
            "primaryContactIndex":self.primaryContactIndex,
            "primaryAddressIndex":self.primaryAddressIndex
        }
    @classmethod
    def deSerialize(cls, data: dict):
        person = cls(data["firstName"], data["lastName"])
        person.primaryContactIndex = data.get("primaryContactIndex", None)
        person.primaryAddressIndex = data.get("primaryAddressIndex", None)

        for contactData in data["contacts"]:
            contact = ContactInfo.deSerialize(contactData)
            person.addContact(contact)

        return person    
    


def loadJsonData(fileName):
    if os.path.exists(fileName):
        with open(fileName, "r") as read:
            
            return json.load(read)
    return []


def saveJsonData(fileName, data):
    with open(fileName, "w") as write:
        json.dump(data, write)

fileName = "outPut.json"
loadedData = loadJsonData(fileName)
peoples = []
print("LOADED DATA ::",loadedData)

if loadedData:
    for personData in loadedData:
        person = Person.deSerialize(personData)
        peoples.append(person)
else:
    print("No data found")

myPerson = Person("Manny","Yadav")
myPerson.addContact(ContactInfo("Phone", "123-456-7890"))
myPerson.addContact(ContactInfo("Email", "mann@gmail.com"))
myPerson.addContact(ContactInfo("Address", "123 Main St, Brampton, CA"),True)
data = myPerson.serialize()
myPerson.setPrimaryContact(0)
myPerson.setPrimaryAddress(2)

myPerson2 = Person("Keerth","Saini")
myPerson2.addContact(ContactInfo("Phone", "123-456-7890"))
myPerson2.addContact(ContactInfo("Email", "keerth@gmail.com"),True)
myPerson2.addContact(ContactInfo("Address", "123 Main St, Brampton, CA"))
myPerson2.setPrimaryContact(1)
myPerson2.setPrimaryAddress(2)
# print(myPerson2.serialize())
data2 = myPerson2.serialize()
finalData =[]
finalData.append(data)
finalData.append(data2)

# with open( "outPut.json" , "w" ) as write:
#     json.dump( finalData , write )
saveJsonData("outPut.json",finalData)


# deSerializedValue = open("outPut.json").read()
# print("Decoded Values",deSerializedValue)


# with open("outPut.json", "r") as read:
#     loadedData = json.load(read)



# for personData in loadedData:
#     person = Person.deSerialize(personData)
#     peoples.append(person)

for person in peoples:
    print(f"Person: {person.firstName} {person.lastName}")
    for contact in person.contacts:
        print(contact)

    # if not len(self.contacts) == 0:
    #         self.primaryContactIndex = len(self.contacts)
    #         print("PRIMARY CONTACT INDEX",self.primaryContactIndex)
        
    #     if not self.primaryContactIndex:
    #         pass
    #     if setPrimary:
    #         # self.primaryContactIndex = len(self.contacts)
    #         pass
    #     self.contacts.append(contact)
    #     # self.numContacts += 1
    #     # self.contacts.append(contact)