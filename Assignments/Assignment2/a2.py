# min=1
# max=10000
# while True:
#     value = input(f"Please enter a number between {min} and {max}: ")
#     if not value.isnumeric():
#         print("This is not a number")
#         continue
#     number = int(value)
#     if(number < min or number > max):
#         print(f"The number is out of range from {min} to {max}")
#         continue
#     break

# factors = []
# factorCount = 0
# if number == 0:
#     factorCount = 0
# elif number == 1:
#     factorCount = 1
#     factors.append(1)
# else:
#     factorCount = 2
#     factors
#     for i in range(2, (number // 2) + 1):
#         if number % i == 0:
#             factors.append(i)
#             factorCount += 1

# print(f"We have found {factorCount} facors for number {number}.")
# if factorCount == 2:
#     print(f"{number} is a prime number")

# while True:
#     value = input("Do you want to see all the factors (y/n) ? :")
#     value = value.lower()
#     if value in ['y', 'n', '']:
#         break
#     print("Invalid input. Please try again using ['Y','y','N','n',''].")


x = 0.01000125
y = 0.00087
v = abs(x - y) > 0.0001
print(abs(x - y))
print(v)