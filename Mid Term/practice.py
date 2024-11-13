print(10 * "-")  
print("Hello", "World")  # Prints with space 
print("Hello" + "World")


print("keerth \n 20")

for i in range (4):
    print('*' * i)

for i  in range (11):
    print(str(i) * i)

for i  in range (11):
    print(i * str(i))

print("hello ---world", sep="---")

name = "John" 
age = 25
height = 1.75 
x = 5       # x is an integer 
x = "John"  # x is now a string 
print(x)

name = "keerth"
age = 22
x = 10
y = 5
x,y = y,x
# y = x
print(f"X {x} Y {y}")

# def calculate_sum(a, b):return a + b 
# print(calculate_sum(3, 4)) 

# age =int (input("Enter your age: ")) 
# if age > 18:
#     print("You are an adult")      

"""print("Divide",5//3)
print("Divide",5%1)"""

print(5 + 3 * 2)    # 11 
print((5 + 3) * 2)  # 16 

x = 1
x += x + 5
x = x + x + 5


# print(5.0 + "5")
x,y = "My name".split()
print(x,y)


list = [1,2,3,4,5,6,7,8,9]
print(list[2:6])

print(0.1 + 0.2)
print(0.3)
print(0.1 + 0.2 == 0.3)


print(round(3.141592))

x = 0.1 + 0.2
y = 0.3
print(abs(x-y)<1e-9)

print(x == 0.3)
print(abs(x - 0.3) < 1e-9)
word = "Python" 
print(word[-1])