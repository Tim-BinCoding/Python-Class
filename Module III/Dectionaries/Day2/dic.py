#1

# dictionary=eval(input())
# average=0
# for key in dictionary:
#     average+=dictionary[key]
# if len(dictionary)>0:
#     print(average/len(dictionary))
# else:
#     print("No teacher here!")

#2

# arrayIndic=eval(input())
# f=0
# m=0
# for dic in arrayIndic:
#     for key in dic:
#         if key.upper()=="FRUIT":
#             f+=1
#         if key.upper()=="MEAT":
#             m+=1
# message="Fruit:" + str(f)+"\n" + "Meat:"+str(m)
# print(message)



#3
# def getMax(arr):
#     # Write your code here
#     maxScore = arr[0]
#     for i in range(len(studentScore)):
#         if studentScore[i]>maxScore:
#             maxScore = studentScore[i]
#     return maxScore

# def getMin(arr):
#     # Write your code here
#     minScore = studentScore[0]
#     for i in range (len(studentScore)):
#         if studentScore[i]<minScore:
#             minScore += studentScore[i]
#     return minScore    

# def getAvg(arr):
#     # Write your code here
#     average = int(maxScore + minScore)/2
#     return average
# # your input here
# studentScore = eval(input())
# maxScore = getMax(studentScore)
# minScore = getMin(studentScore)
# average = int(getAvg(studentScore))
# result = {"max":maxScore,"min":minScore,"avg":average}
# print(result)

#4

# studentsData =eval(input())
# name=""
# smallthan=False
# message="No result"
# if len(studentsData)>0:
#     maxScore=0
#     for dic in studentsData:
#         if dic['score']>maxScore and dic['score']>75:
#             maxScore=dic['score']
#             name=dic['name']
#             message="The best student is "+str(name)+'\n' + 'All students have more than '+str(75)
#         elif dic['score']<75:
#             smallthan=True
#     if smallthan:
#         message="The best student is "+str(name)
# print(message)


# ------ Reviews -----------

#1
# dectionary={}
# average=0
# if len(dectionary)>0:
#     for key in dectionary:
#         average+=dectionary[key]
#     average=average/len(dectionary)
#     print(average)
# else:
#     print("Not teacher here!")


#riviewHolloweencup

#2
# list1=[1,3,5,6,7,9,10,13,15,17,19,20,21,23,16,29,30,31]
# list2=[13,3,17,19,20,21,23,16,29,30,31,5,6,7,9,10,13,15]
# list3=[15,17,19,20,21,1,3,5,6,7,9,10,13,23,16,29,30,31]
# list4=[9,10,1,3,5,6,7,13,15,17,19,20,21,23,16,29,30,31]
# list5=[21,23,16,29,1,3,5,6,7,9,10,13,15,17,19,20,30,31]
# realBorn=input()
# sumOfdate=0
# for i in range(5):
#     if realBorn=="true" and i==0:
#         sumOfdate +=list1[0]
#     if realBorn=="true" and i==1:
#         sumOfdate +=list2[0]
#     if realBorn=="true" and i==2:
#         sumOfdate+=list3[0]
#     if realBorn=="true" and i==3:
#         sumOfdate+=list4[0]
#     if realBorn=="true" and i==4:
#         sumOfdate +=list5[0]
# if sumOfdate==0:
#    sumOfdate="The day has to be appaered in one list of number at least"
# print(sumOfdate)

#2

# word="good"
# newDic={}
# for i in word:
#     if i!=" ":
#         if i in newDic:
#             newDic[i]+=1
#         else:
#             newDic[i]=1
# print(newDic)

#2

# arrayDiction=eval(input())
# totalOfamont=0
# for dic in arrayDiction:
#     totalOfamont+=dic["price"]*int(dic["quantity"])
# print(totalOfamont)


#3
# nameOfingredient=input()
# quantityOfvalue=int(input())
# arrayDiction=eval(input())
# payEnuoght=False
# for dic in arrayDiction:
#     if dic["ingredient"]==nameOfingredient:
#         if dic["quantity"]- quantityOfvalue>=0:
#             payEnuoght=True
#             dic["quantity"]=dic["quantity"] - quantityOfvalue
# if payEnuoght:
#     print(arrayDiction)
# else:
#     print("There is not enough stock in the kitchen for this ingredient")
