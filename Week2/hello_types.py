num1 = 1
num2 = 4
num3 = num1 + num2

print("NUM3",num3)
# //optimize FLOATS
float1 = 1.0
float2 = 0.5
float3 = float1 + float2
print("FLOAT3",float3)

# //optimize Strings
string1 = "1"
string2 = "1"
string3 = string1 + string2
print("String3",string3)

# //optimize Mix
mix1 = num1 + float1
# mix2 = string1 + num1
# mix3 = float1 + string1
# print("mix1",mix1,"mix2",mix2,"mix3",mix3)
print("mix1",mix1)
print("TRY :",4.0/2.0)

num1 = 4
print(num1,type(num1))
num1 = num1/2               #now num1 is changed to type float
print(num1, type(num1))
num1 = int(num1)            #now num1 is changed to type float
print(type(num1))   #with integers all the numbers after deicmals are truncated ex. 2.999999 is 2 only the remaining .99999 is truncated 

print("Type check",type(int("1")))
# print(float("zero"))
print(str(4))
# print(int("Hello World"))