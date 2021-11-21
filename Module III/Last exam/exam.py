#1

# array = eval(input())
# newArray=[]
# for value in array:
#     if (value>=10 and value<=35) or (value>=-35 and value<=-10):
#         newArray.append(value*(-1))
#     elif value<10 or value>35:
#         newArray.append(value)
# print(newArray)


#2
# array2D=[[1, -3, -8], [4, -9, 5], [-12, 8, -7]]
# for row in array2D:
#     for col in range(len(row)):
#         if row[col]<3 and row[col]>0:
#             row[col]="#"
#         elif row[col]>=6 and row[col]<9:
#             row[col]="@"
#         elif row[col]<0:
#             row[col]="$"
# print(array2D)

#3
# array=eval(input())
# sumArray=0
# newArray=[]
# isValid=False
# n=0
# while not isValid and n<len(array):
#     if sumArray<100:
#         sumArray+=array[n]
#         newArray.append(array[n])
#     else:
#             isValid=True
#     n+=1
# if sumArray<100:
#     newArray=[]
# print(newArray)


#4
# listOfPersonns = [['ronan', 'Ogor', 22],['Jonathan', 'Faucher', 17],['Sievny', 'Nav', 8],['Seiha ', 'Hi', 86]]
# for row in listOfPersonns:
#     for col in range(len(row)):
#         if row[2]<18:
#             row.append("minor")
#         elif row[2]>=18:
#             row.append("major")
# print(listOfPersonns)

