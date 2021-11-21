# def average(scores):
#     #TODO
#     scoreOfaverage=0
#     numberscore=0
#     getAverage=0
#     for i in scores:
#         scoreOfaverage+=i
#         numberscore+=1
#     getAverage+=scoreOfaverage/numberscore 
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# numberOfstudent=int(input())
# for n in range(numberOfstudent):
#     getScores=eval(input())
# gatAllAverage=average(getScores)
# print(gatAllAverage/numberOfstudent)


# CORRECTOIN EXAM 6

#1
# def contains(word,char):
#     foundThesametext=False
#     for i in range(len(word)):
#         if word[i].upper()==char.upper():
#             foundThesametext=True
#     return foundThesametext
# word=input()
# char1=input()
# char2=input()
# message="NOT VALID"
# if contains(word, char1)and contains(word, char2):
#     message="VALID"
# print(message)

#2
# def reverse(text):
#     valueRever=text[::-1]
#     return valueRever
# reverseOftext=input()
# print(reverse(reverseOftext))

#####2
# def reverse(text):
#     textRever=""
#     for i in range(len(text)):
#         textRever+= text[len(text)-1-i]
#     return textRever
# text=input()
# print(reverse(text))

##3

# def multiplyWithinRange(startNumber, endNumber):
#     value=1
#     if startNumber< endNumber:
#         for n in range(startNumber, endNumber+1):
#                 value=value*n
#     else:
#         value=value*0
#     return value
# firstNumber=int(input())
# lastNumber=int(input())
# print(multiplyWithinRange(firstNumber, lastNumber))

#4
# def CountChar(word,char):
#     foundThesametext=0
#     for index in (word):
#         for i in range(len(index)):
#             if index[i].upper()==char.upper():
#                 foundThesametext +=1
#     return foundThesametext
# charater=input()
# words = eval(input())
# print(CountChar(words,charater))

#5
# def allAverage(scores):
#     toTall=0
#     for i in range(scores):
#         listScore=eval(input())
#         scoreInList = 0
#         for i in listScore:
#             scoreInList += i
#         toTall += scoreInList/len(listScore)
#     return toTall/numbers
# numbers=int(input())
# print(allAverage(numbers))

#1

# def averageOnestudent(averageOne):
#     value=0
#     for i in averageOne:
#         value+=i
#     return int(value/len(averageOne))
# def allAverage(score):
#     toTallAverage=0
#     for i in range(score):
#         listScore=eval(input())
#         toTallAverage += averageOnestudent(listScore)
#     return toTallAverage / numberOfstudents
# numberOfstudents=int(input())
# print(allAverage(numberOfstudents))
 

# #5

# def sumScore(numbers):
#     	total = 0
# 	for value in numbers:
# 		total += value
# 	return total

# def average(totalScore, length):
# 	average = 0
# 	average = totalScore/length
# 	return average


# numberStudents = int(input())
# totalAverage = 0
# totalScoreOfStudent = 0
# finalAverage = 0
# for i in range(numberStudents):
# 	scoreOfstudent = eval(input())
# 	totalScoreOfStudent = sumScore(scoreOfstudent)
# 	totalAverage += average(totalScoreOfStudent, len(scoreOfstudent))

# finalAverage = average(totalAverage, numberStudent)