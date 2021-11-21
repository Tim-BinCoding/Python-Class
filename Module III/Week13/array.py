# ex1

# a=[1,2,3]
# a[0]=7
# b=[a[0],a[1],a[2]]
# print(b[0])

# let's add elements!!
# number=[10,20,30]
# number.append(50)

#EX2

# oddNumber=[]
# for i in range(5):
#     inputOfnumber=int(input())
#     if inputOftext%2 == 1:
#       oddNumber.append(inputOfnumber)
# print(oddNumber)


# LET'S INSERT ELEMENTS!

#EX3

# numbers=[10,20,30]
# numbers.insert(1,15)
# print(numbers)

# remove number 3 from array

#ex3
# numbers = [6,3,4,3,2,5,3,5]
# removeNumber=0
# for i in numbers:
#     if i == 3:
#         numbers.pop()
#     removeNumber+=1
# print(numbers)    
    
# def isEqual(list1, list2) :
#     return "NOT EQUAL" 
#     for n1 in range(len(list1)):
#         for n2 in range(len(list2)):
#             if n1==n2 and list1[n1][0]==list2[n2][0] and list1[n1][1]==list2[n2][1]:
#                 return "EQUAL"
# list1 = eval(input())
# list2 = eval(input())
# print(isEqual(list1,list2))


# listOfnumber=[1,1,1,2,3,4,4]
# numberRemove=0
# for i in range(1,len(listOfnumber)):
#     if listOfnumber[i-1]==listOfnumber[i]:
#         listOfnumber.pop(numberRemove)
#         numberRemove+=1
# print(listOfnumber)

# listOfnumber=eval(input())
# newNumber=[listOfnumber[0]]
# for i in range(1,len(listOfnumber)):
#     oldNumber=listOfnumber[i-1]
#     if listOfnumber[i]!= oldNumber:
#         newNumber.append(listOfnumber[i])
# print(oldNumber)


# numberInput=eval(input())
# numberGreater=0
# for i in range (1,len(numberInput)):
#     oldNuumber=numberInput[i-1]
#     if numberInput[i]>oldNuumber:
#         numberGreater+=1
# print(numberGreater)      


# #1
# def isEqual(list1, list2) : 
#     if len(list1)==len(list2):
#         for i in range(len(list1)):
#             if list1[i]!=list2[i]:
#                 return False
#         return True
#     return False
# list1=eval(input())
# list2=eval(input())
# if isEqual(list1,list2):
#     print("EQUAL")
# else:
#     print('NOT EQUAL')

# #2
# listOfnumber=eval(input())
# newNumber=[listOfnumber[0]]
# for i in range(1,len(listOfnumber)):
#     oldNumber=listOfnumber[i-1]
#     if listOfnumber[i]!= oldNumber:
#         newNumber.append(listOfnumber[i])
# print(newNumber)

#3
# numberInput=eval(input())
# numberGreater=0
# for i in range (1,len(numberInput)):
#     oldNuumber=numberInput[i-1]
#     if numberInput[i]>oldNuumber:
#         numberGreater+=1
# print(numberGreater)      

#4
# array=eval(input())
# name=input()
# array.append(name)
# print(array)

#reviews exercise

#1

# list1=eval(input())
# list2=eval(input())
# conditoin=False
# if len(list1)==len(list2):
#     for i in range(len(list1)):
#         if list1[i]!=list2[i]:
#             conditoin=False
#         else:
#             conditoin=True
# if conditoin:
#     print("EQUAL")
# else:
#     print("NOT EQUAL")

# SOLUTOIN 2 USE FUNTOIN

# def isEqual(list1,list2):
#     if len(list1)==len(list2):
#         for i in range(len(list1)):
#             list1[i]=list2[i]
#         return True
#     return False
# list1=eval(input())
# list2=eval(input())
# realConditoin=isEqual(list1, list2)
# if realConditoin:
#     print("EQUAL")
# else:
#     print("NOT EQUAL")




# def splitBySpace(theString) :
#     words = []
#     currentWord =""
#     number=0
#     for character in range(len(theString)):
#         if theString[character] == " " :
#             currentWord = theString[number:character]
#             if (len(currentWord)>0) :
#                 number = character
#                 words.append(currentWord)               # We add the word only if not
#                 currentWord = "" 
#     else:
#         words.append(theString)       
#                                 # We reset the current word
#         #     else :
#         #         currentWord += character                 #maybe need to add the last word
#         # elif (len(currentWord) > 0) :
#         #     words.append(currentWord)
#     return words                                                    # MAIN CODE
# word = input()                                                       # Write your code here !
# print( splitBySpace(word))

#ex1
# array=eval(input())
# for number in range(len(array)):
#     if array[number]<10:
#         array[number]=10
# print(array)

#ex2
# array=eval(input())
# newArray=input()
# array.append(newArray)
# print(array)


#ex3
# def transferArray(array):
#     newArray=[]
#     for i in range(len(array)):
#         newArray.append(array[i]+1)
#     return newArray
# array=eval(input())
# print(transferArray(array))

#ex4
# def findIndexOfSeven(array): 
#     index=[]
#     for number in array:
#         if number!=7:
#             index.append(number)
#     return index
# array = eval(input())
# print(findIndexOfSeven(array))

#ex5
# def replaceZero(array):
#     newArray=[]
#     for number in range (len(array)):
#         if array[number]==1:
#             newArray.insert(number,0)
#         else:
#             newArray.append(array[number])
#     return newArray
# array=eval(input())
# print(replaceZero(array))



#HackerRank Part II
#3

# def findIndexOfSeven(array):
#     #write your code here: 
#     index=[]
#     for number in array:
#         if number!=7:
#          index.append(number)
#     return index
# array = eval(input())
# #write your code here.
# print(findIndexOfSeven(array))

#1
# array=eval(input())
# char=[]
# for index in array:
#     for i in index:
#         if i not in char:
#           char.append(i)
#     char.sort()   
# print(char)

#2
# def getMinimumindex(array):
#     initialList=[]
#     for i in array:
#         if i not in initialList:
#             initialList.append(i)
#     initialList.sort()
#     return initialList
# array=eval(input())
# print(getMinimumindex(array))

#2
# def getMinimumIndex(list1):
#     minIndex=0
#     numList=list1[0]
#     for i in range(1,len(list1)):
#         if list1[i]<numList:
#             minIndex=i
#             numList = list1[i]
#     return minIndex
# def remove(array):
#     newArray=[]
#     for i in range(len(array)):
#         newArray.append(array[getMinimumIndex(array)])
#         array.pop(getMinimumIndex(array))
#     return newArray
# array=eval(input())
# print(remove(array))


#3
# def findIndexOfSeven(array):
#     #write your code here: 
#     index=[]
#     for number in array:
#         if number!=7:
#          index.append(number)
#     return index
# array = eval(input())
# #write your code here.
# print(findIndexOfSeven(array))

#4
# array=eval(input())
# for numbers in array:
#     for i in range(len(numbers)):
#         if numbers[i]==7:
#             numbers[i]=8
# print(array)

#5
# array=eval(input())
# newArray=[]
# for i in array:
#     if i not in newArray:
#         newArray.append(i)
# numberOfarray=""
# for numbers in newArray:
#     numberOfarray+= str(numbers) + " "
# print(numberOfarray)
    

#corretoin with teacher
#1

# array=eval(input())
# charOftext=[]
# for word in array:
#     for char in word:
#         if char not in charOftext:
#             charOftext.append(char)
#     charOftext.sort()
# print(charOftext)

#5

# initailist=eval(input())
# orderList=[]
# def getMinimumIndex(numbers):
#     miniMumNumber=numbers[0]
#     rangNumber=0
#     for i in range(1,len(numbers)):
#         if miniMumNumber > numbers[i]:
#             miniMumNumber = numbers[i]
#             rangNumber=i
#     return rangNumber
# for i in  range(len(initailist)):
#     orderList.append(initailist[getMinimumIndex(initailist)])
#     initailist.pop(getMinimumIndex(initailist))
# print(orderList)

#1
# def numberOfEight(array):
#     # Enter your code here:
#     numOf8 = 0
#     for num in array:
#         if num == 8:
#             numOf8 +=1
#     return numOf8
# #Enter your code here:
# array=eval(input())
# if (numberOfEight(array))!=0:
#     print(numberOfEight(array))
# else:
#     print("NOT FOUND")

#2

# array= eval(input())
# name=input()
# indexAdd=int(input())
# array.insert(indexAdd,name)
# print(array)

# def format_string_to_array(string):
#     array = []
#     array_item = ""
#     is_quote = False
#     i = 0
#     while i < len(string):
        
#         if string[i:i+1] == " ":
#             # Character is a space
#             if is_quote == True:
#                 # If quote, add character to array_string
#                 array_item += string[i]
#             elif is_quote == False:
#                 # When word is finished
#                 if not array_item == "":
#                     # If array does not equal nothing, append
#                     array.append(array_item)
#                     array_item = ""
#         elif string[i:i+1] == "\"" or string[i:i+1] == "\'":
#             # Character is a quote
#             if is_quote == False:
#                 is_quote = True
#             else:
#                 array.append(array_item)
#                 array_item = ""
#                 is_quote = False
#         else:
#             # Character is normal
#             array_item += string[i]

#         i += 1
#     array.append(array_item)
#     return array

# a = "Hello \'single array item with spaces\' World!"
# print(format_string_to_array(a))


# def splitBySpace(text):
#     #write your code here
#     array

#3

# def splitBySpace(text):
#     array = []
#     index = ''
#     for i in text:
#         if i == ' ':
#             array.append(index)
#             index = ''
#         else:
#             index += i
#     if index:
#         array.append(index)
#     return array
# text=input()
# print(splitBySpace(text))

#4

# array=eval(input())
# oddArray=[]
# for i in array:
#     if i%2==1:
#         oddArray.append(i)
# reverOddNumber=[]
# for n in range(len(oddArray)):
#     reverOddNumber.append(oddArray[len(oddArray)-1-n])
# print(reverOddNumber)

#5

# array=eval(input())
# newArray=[]
# for i in range(len(array)):
#     if array[i]<5:
#         newArray.insert(i, max(array))
#     else:
#         newArray.append(array[i])
# print(newArray)

#1
# word=input()
# numberA=0
# numberB=0
# numberC=0
# for i in word:
#     if i=="a" or i=="A":
#         numberA+=1
#     if i=="b" or i=="B":
#         numberB+=1
#     if i=="c" or i=="C":
#         numberC+=1
# result=0
# if numberA==4:
#     result=40
# elif numberA==numberB==2 :
#     result=20
# elif numberC>=1:
#     result=10
# print(result)

#2
# def sumOfindex(text):
#     sumOfcharX=0
#     for i in range(len(text)):
#         if text[i]=="x" or text[i]=="X":
#             sumOfcharX +=i
#     return sumOfcharX
# word=input()
# print(sumOfindex(word))

#3
# def findFirstX(text):
#     firstX=0
#     firstY=0
#     message="GOOD"
#     for i in range(len(text)):
#         if text[i]=="X":
#             firstX=i
#         if text[i]=="Y":
#             firstY=i
#     if firstY<firstX or firstX == firstY ==0 :
#         message="NOT GOOD"
#     return message
# charater=input()
# print(findFirstX(charater))



# STRAGTERGIES2
# def findXBeforY(word):
#     xBeforY = False
#     yBeforX = False
#     for i in range(len(word)):
#         if word[i] == "X" and not xBeforY and not yBeforX:
#             xBeforY = True
#         elif word[i] == "Y" and not yBeforX:
#             yBeforX = True
#     xAndY = xBeforY and yBeforX
#     return xAndY
# word = input()    
# result = "NOT GOOD"
# if findXBeforY(word):
#     result = "GOOD"
# print(result)
        
#3
  
# def getLastIndex(word, char):
#     result = -1      
#     for i in range(len(word)):
#         if word[i] == char:
#             result = i
#     return result

# word = "XYX"
# indexX = getLastIndex(word, "X")
# indexY = getLastIndex(word, "Y")

# if indexX!=-1 and indexY!=-1 and indexY> indexX :
#     print("GOOD")
# else :
#     print("NOT GOOD")


