
#1

# print( len( ["ronan","pnc"] ) )

#2

# array = [1, 2, 3, 4, 5]
# for index in range(len(array)):
#     value = array[index]
#     print("hello " + str(value))
# print("The finnished at:  "+str(len(array)))


#3

# myArray=[12,13,15,16,3]
# myElement=myArray[3]
# print(myElement)

#4

# array=[3,3,3,4]
# array.reverse()
# print(array)

#4

# list1=[3,2,1]
# list2=list1
# list1[0] = 99
# print(list1[0])
# print(list2[0])
#answers
# 99
# 99

#ex1

# def numberOfSevens(numbers):
#     sumOfSeven=0
#     for value in numbers:
#         if value==7:
#             sumOfSeven += 1
#     return sumOfSeven
# numbers=eval(input("Value: "))
# print(numberOfSevens(numbers))

#ex2

# def sumOfGreaterPrevois(numbers):
#     preNumber=numbers[0]
#     sumOfGreater=0
#     for value in range(len(numbers)):
#         nextNumber=numbers[value]
#         if value>0 and nextNumber>preNumber:
#             sumOfGreater +=1
#             nextNumber = preNumber
#         else:
#             preNumber=numbers[value]
#     return sumOfGreater
# numbers=eval(input("Enter value: "))
# print(sumOfGreaterPrevois(numbers))

#ex3

# def countA(text):
#     textOfelement=""
#     sumOfA=0
#     for i in text:
#         textOfelement=i
#         for char in textOfelement:
#             if char=="a" or char=="A":
#                 sumOfA +=1
#             else:
#                 sumOfA +=0
#     return sumOfA
# text=eval(input("Input: "))
# print(countA(text))


#ex4

# def getIndxOfCountry(countryName):
#     for index in range(len(countries)):
#         if countries[index] == countryName.lower():
#             return index
#     return -1
# countries = ["canada", "france", "usa", "cambodia"]
# countryPopulationInMillions = [110, 70, 250, 8]
# nameCountry = input("Enter country: ")
# result = ""
# indexOfCountry = getIndxOfCountry(nameCountry)
# if (indexOfCountry) > -1:
#     result = "Population of "+ nameCountry +" is "+ str(countryPopulationInMillions[indexOfCountry]) +" millions people"
# else:
#  result = "Country not found"
# print(result)

# lisOfcities=["pvh","kpt","kd","smr"]
# amonOfcitizen=[100,130,300,200]
# def foundCity(nameOfcity):
#     for element in range(len(lisOfcities)):
#         if lisOfcities[element]==nameOfcity:
#             return element
#     return -1
# nameOfcity=input("enter: ")
# metCity = foundCity(nameOfcity)
# if metCity>-1 :
#     result="The people live in "+str(nameOfcity) + "is "+str(amonOfcitizen [metCity]) + " citizen"
# else:
#     result="Not found"
# print(result)


#ex5
  
# def realSentence(word):
#     result=""
#     numbers=eval(input("Enter the order of words :"))
#     for i in range(len(numbers)):
#         for index in range(len(word)):
#             if index==numbers[i]:
#                 result=result+word[index]
#         result=result+" "
#     return result
# word=eval(input("Enter words:"))
# print(realSentence(word))

#1

# def sumArray(array):
#     sumOfarray1=0
#     sumOfarray2=0
#     for i in array:
#         sumOfarray1 +=i
#     return sumOfarray1
#     for i in array:
#         sumOfarray2 +=i
#     return sumOfarray2
# array1 = eval(input())
# array2 = eval(input())
# array1=sumArray(array1)
# array2=sumArray(array2)
# print(int(array1+array2))

#2
# def numberOfEight(array):
#     sumOfEight= 0
#     for i in array:
#         if i == 8 :
#             sumOfEight +=1 
#     if sumOfEight==0:
#         return "NOT FOUND"
#     return sumOfEight
# array=eval(input())
# print(numberOfEight(array))

#3

# def indexOfarray(array,indexOfitem):
#    item=array[indexOfitem]
#    return item
# array = eval(input("enter: "))
# indexOfitem= int(input("index: "))
# print(indexOfarray(array,indexOfitem))


#ex4
# def countEven(array):
#     numOfEven = 0
#     for i in array:
#         if i%2 == 0:
#             numOfEven +=1
#     return numOfEven
# def countOdd(array):
#     numOfOdd = 0
#     for i in array:
#         if i%2==1:
#             numOfOdd +=1
#     return numOfOdd
# array1 = eval(input())
# print("EVEN: " +str(countEven((array1))))
# print("ODD: " +str(countOdd((array1))))


#3

# # def finItem(text):
# #     listItem = text[numberOfItem]
# #     return listItem
# listItem=["mose","Like","hello"]
# # listItem=eval(input())
# numberOfItem=int(input())
# # print(finItem(numberOfItem))
# print(listItem[numberOfItem])

#ex4

# def findEven(numbers):
#     numOfEven = 0
#     for i in range(len(numbers)):
#         if numbers[i] % 2 == 0:
#             numOfEven +=1
#     return numOfEven
# def findOdd(numbers):
#     numberOfOdd=0
#     for i in range(len(numbers)):
#         if numbers[i] % 2 == 1:
#             numberOfOdd += 1
#     return numberOfOdd
# array=eval(input("Array: "))
# print("Even: "+str(findEven(array)))
# print("Odd: "+ str(findOdd(array)))

# def isEqual(list1,list2):
# list1=eval(input("list1: "))


#dx1  
# def isEqual(lists):
#     numberisEqual= "NOT EQUAL"
#     for i in range(len(lists)):
#         for n in range(len(lists)):
#             if i != n and lists[i][0] == lists[n][0] and lists[i][1]==lists[n][1]:
#                 numberisEqual = True
#     return "EQUAL"
# value=eval(input("list: "))
# print(isEqual(value))

#EX2

# lisOftext=eval(input())
# sumOfGreater=0
# for i in range(1,len(lisOftext)):
#     if lisOftext[i-1]<lisOftext[i]:
#         sumOfGreater +=1
#     else:
#         sumOfGreater+=0
# print(sumOfGreater)
#reviews exercise

#1

# def numberOfSevens(numbers):
#     countOfSeven="NOT FOUND"
#     for i in range(len(numbers)):
#         if numbers[i]==7:
#             countOfSeven+=1
#     return str(countOfSeven)
# array=eval(input())
# print(numberOfSevens(array))

#2
# def countGreater(ngreater):
#     sumOfgreater=0
#     for i in range(1,len(ngreater)):
#         if ngreater[i-1]<ngreater[i]:
#             sumOfgreater+=1
#     return sumOfgreater
# numbers=eval(input())
# print(countGreater(numbers))


# countryNames = ["canada", "france", "usa", "cambodia"]
# countryPopulationInMillions = [110, 70, 250, 8]
# getindexOfCountry=input()
# for i in range(len(countryNames)):
#     if countryNames[i]==getindexOfCountry:
#         countIndex = i
# country=countryPopulationInMillions[countIndex]
# print("The Country "+ str(getindexOfCountry) +" : "+ str(country))

#ex4

# def realSentence(word):
#     result=""
#     numbers=eval(input("Enter the order of words :"))
#     for i in range(len(numbers)):
#         for index in range(len(word)):
#             if index==numbers[i]:
#                 result=result+word[index]
#         result=result+" "
#     return result
# word=eval(input("Enter words:"))
# print(realSentence(word))


#5

# def getListOfchar(listChar,order):
#     indexOfchar=""
#     for i in order:
#         for n in range(len(listChar)):
#             if i == n:
#                 indexOfchar +=listChar[n] 
#         indexOfchar+=" "
#     return indexOfchar
# charater=eval(input("Text: "))
# numberOflistchar=eval(input("number: "))
# print(getListOfchar(charater,numberOflistchar))

     
