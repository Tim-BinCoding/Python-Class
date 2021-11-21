#1

# def removeSevens(numbers): 
#  result = [] 
#  for value in numbers: 
#     if value != 7: 
#         result.append(value) 
#  return result 
# # MAIN CODE 
# values = eval(input()) 
# print(removeSevens(values))

#ex2

# def sum2By2number(numbers): 
#     result = [] 
#     for value in range(1,len(numbers)): 
#             result.append(numbers[value-1]+numbers[value])
#     return result 
# values = eval(input()) 
# print(sum2By2number(values))


#ex3
# values = eval(input()) 
# hasPair=False 
# for i in range(len(values)) : 
#  for j in range(len(values)) : 
#     if i!=j and values[i] == values[j] : 
#         hasPair =True 
# if hasPair: 
#     print("HAS PAIR") 
# else: 
#     print("HAS NO PAIR")
# # MAIN CODE
#   


#ex4
# MAIN CODE
#   
# values = eval(input()) 
# hasPair=False 
# for index1 in range(len(values)) : 
#  for index2 in range(len(values)) : 
#     value1 = values[index1][0] 
#     color1 = values[index1][1] 
  
#     value2 = values[index2][0] 
#     color2 = values[index2][1] 
  
#     if index1!=index2 and value1==value2 and color1==color2 :
#         hasPair =True 
# if hasPair: 
#  print("HAS PAIR") 
# else: 
#  print("HAS NO PAIR")


# text=input()
# numOfCharA=0
# numOfCharB=0
# for i in text:
#     if i=='a' or i=="A":
#         numOfCharA+=1
#     elif i=="b" or i=="B":
#         numOfCharB+=1
# if numOfCharA==numOfCharB and numOfCharA==2:
#     print("Good")
# else:
#     print("Bad")



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
    

    





