#1
# list1=eval(input())
# list2=eval(input())
# message="NOT EQUAL"
# numberSame=0
# if len(list1)==len(list2):
#     for i in range(len(list1)):
#         if list1[i]==list2[i]:
#             numberSame+=1
#     if numberSame==len(list1):
#         message="EQUAL"
# print(message)

# ------ review exam ----

#1

# def checkIndex(index,check):
#     hasCheck=False
#     for i in range(len(index)):
#         if index[i].upper()==check.upper():
#             hasCheck=True
#     return hasCheck
# def checkSecon(index,checkAgain):
#     hasCheckAgain=False
#     for i in range(len(index)):
#         if index[i].upper()==checkAgain.upper():
#             hasCheckAgain=True
#     return hasCheckAgain
# index=input()
# check=input()
# checkAgain=input()
# message="Not valid"
# if checkIndex(index, check) and checkSecon(index, checkAgain):
#     message="Valid"
# print(message)

#2

# def reverIndex(index):
#     revese=""
#     for i in range(len(index)):
#         revese+=index[len(index)-1-i]
#     return revese
# index=input()
# print(reverIndex(index))

#3
# def multiplyWithinRang(start,end):
#     value=1
#     for n in range(start, end+1):
#         value*=n
#     return value
# start=int(input())
# end=int(input())
# print(multiplyWithinRang(start, end))

#4

# def countChar(word,char):
#     countOneChar=0
#     for index in word:
#         for i in index:
#             if i.upper()==char.upper():
#                 countOneChar+=1
#     return countOneChar
# word=input()
# char=input()
# print(countChar(word, char))

#5
# def averageAll(listNumber):
#     allAverage=0
#     for value in listNumber:
#         averaOneList=0
#         for n in value:
#             averaOneList+=n
#         allAverage+=averaOneList/len(value)
#     allAverage=allAverage/len(listNumber)
#     return int(allAverage)
# listNumber=eval(input())
# print(averageAll(listNumber))

