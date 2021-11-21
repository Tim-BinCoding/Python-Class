

# #1

# def numberOfUpperCase(text):
#    isUppercase=0
#    for i in range(len(text)):
#        if "A"<=text[i] <= "Z":
#            isUppercase += 1
#    return isUppercase
# text=input("Word: ")
# print("Number Of upper case letter " + str( numberOfUpperCase(text)))

# #2
# def getComment(grade):
#     if grade>10:
#         return "Good"
#     return "Bad"
# print(getComment(12) + getComment(8))

# #2,2

# def getComment(grade):
#     if grade>10:
#         return "Good"
#     else:
#         return "Bad"
# print(getComment(12) + getComment(8))


# #3

# def getPrice(fruitName):
#     getDolla=0
#     if fruitName=="Banana":
#         getDolla=2
#     if fruitName=="Apple" :
#         getDolla=5
#     if fruitName=="Orange":
#         getDolla=1
#     return getDolla
# print("Banana price is: " +str(getPrice("Banana")) + " dolla")
# print("Orange price is: " +str(getPrice("Orange")) + " dolla")

# #4

# def getAbsolute(number):
#     if number< 0:
#         return -1* number
#     else:
#         return number
# print(getAbsolute(5) + 10)

# #5

# #test1
# number1 = 20
# number2 = 100
# result=0
# def max(number1,number2):
#     if number1 > number2:
#         result = number1
#     else:
#         result = number2
#     return result
# print("Maximum is " + str(max(number1, number2)))

# #test2
# number1 = 200
# number2 = 300
# print("Maximum is " + str(max(number1, number2)))

# #6
# # test1

# def reverseString(word):
#     for i in range(len(word)):
#         return word[:: -1]
# text1="Hello PNC"

# #test2
# print(reverseString(text1))
# text2="Class 2022"
# print(reverseString(text2))

# #6,2
# #test1

# def reverseString(word):
#     result=""
#     lastIndex=len(word)-1
#     for i in range(len(word)):
#         result+= word[lastIndex-i]
#     return result
# text1="Hello PNC"

# #test2

# print(reverseString(text1))
# text2="Class 2022"
# print(reverseString(text2))