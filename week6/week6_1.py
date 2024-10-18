def listtops():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    #slice opeartions
    print("l1[0:5]",   l1[0:2])
    print("l1[0:10]",  l1[1:2]) #first number is starting index and second number is one greater than the ending index
    print("l1[5:10]",  l1[:5]) # if we don't enter a starting index, it will start from the beginning
    print("l1[5:10]",  l1[2:]) # if we don't enter an ending index, it will go till the end
    print("li[::-1]",  l1[::-1])
    print("li[::2]",   l1[::2])
    print("li[1::2]",  l1[1::2])
    print("li[0:10:3]",l1[0:10:3])

listtops()



