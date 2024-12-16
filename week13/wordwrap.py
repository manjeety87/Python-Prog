class Greeting:
   def __init__(self, name):
      self.name = name

   def say_hello(self):
      print(f"Hello, {self.name}!")

# Instantiate the class
greet = Greeting("Sheridan")
greet.say_hello()
































































# # file = open("WW_0.txt", "r")
# # print(file)

# sentence1 = "Spiderman Spiderman does whateveraspider can"
# breakBy = 14
# temp = sentence1.split(" ")
# for word in (temp):
#     remaingSpace = 14 - len(word)
#     # print(remaingSpace)
#     # print(remaingSpace  > len(word))
#     # print(word[:breakBy],remaingSpace, end="\n")
#     if remaingSpace > len(word):
#         # print(14 -len(word))
#         print(word[:breakBy],remaingSpace, end="\n")
#     else:
#         print(word[breakBy:],end="\n")
#         # word = word[breakBy:]
#     # print(word, end="\n")
#     #  if len(word) > breakBy:
#     #       print(word[:breakBy], end="\n")
# # if len(sentence1) > breakBy:
# #     print(sentence1[:14], end="\n")
# #     sentence1 = sentence1[14:]
# #     print(sentence1[:14], end="\n")
# #     sentence1 = sentence1[14:]
# # print(sentence1[:14])

# # splittedLine = sentence1.split(" ")
# # print(splittedLine)
# # for i in range(len(splittedLine)):
# #     print(splittedLine[i][:14], end="\n")
#     # if len(splittedLine[i]) > 14:
#     #     print(splittedLine[i][14:], end="\n")
#     # else:
#     #     print((splittedLine[i]), end="\n")



# def wordWrap(sentence1,wordWrapByCharacter):
#     # print(sentence1[:14], end="\n")
#     # if(len(sentence1) > wordWrapByCharacter):
#     #     print("TEST",sentence1.split(" "))
#     #     print()
#         if sentence1[wordWrapByCharacter] == " ":
#         #     print(sentence1[:wordWrapByCharacter], end="\n")
#         #     sentence1 = sentence1[wordWrapByCharacter:]
#             print(sentence1[:wordWrapByCharacter], end="\n")
#             wordWrap(sentence1[wordWrapByCharacter:],wordWrapByCharacter)
#         # print(sentence1[:wordWrapByCharacter], end="\n")
#         # sentence1 = sentence1[wordWrapByCharacter:]
#         # print(sentence1[:wordWrapByCharacter])
#         # sentence1 = sentence1[wordWrapByCharacter:]
#         # print(sentence1[:wordWrapByCharacter])
#         # sentence1 = sentence1[wordWrapByCharacter:]
#         # print(sentence1[:wordWrapByCharacter])

# # wordWrap(sentence1,14)
# # for i in range(len(sentence1)):
# #     while len(sentence1) > 14:
# #         print(sentence1[i], sep="\n")
#     # if i == 14:
#     #     print(sentence1[i], end="\n")