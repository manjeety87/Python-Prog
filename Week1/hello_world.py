# print("Hello" , "World")
# print("Manjeet")`

myNum = 87
yourNum = 8
yourNumString = '81'
booleanString = False
ourNum = myNum + yourNum
# print("Addition of numbers are :",ourNum)


def func(courseCode,courseName = ''):     # courseName here is an argument
    print("Manjeet is in which course ?",courseCode,courseName)


func("CS10095")  # -> Computer Programming here is as parameter
func("Computer Programming", "CS10095")  # -> Computer Programming here is as parameter
print("Hello" , "World")

def chef(chef1, chef2, chef3):
    return chef1 + chef2 + chef3
    
vaibhav = chef(10,20,30)
# print(type(yourNumString))
print(vaibhav)


name = "Manjeet's name is : Manjeet"
print(name)