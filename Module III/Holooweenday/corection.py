
# -------- Holooween1 ------

#1

# array=eval(input())
# oddArray=[]
# for i in range(len(array)):
#     if i%2==1:
#         oddArray.append(array[i])
# print(oddArray)

#------ --- fontion --------

# def getOddarray(array):
#     oddArray=[]
#     for i in range(len(array)):
#         if i%2==1:
#             oddArray.append(array[i])
#     return oddArray
# array=eval(input())
# print(getOddarray(array))


#2

# list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25,27, 29, 31]
# list2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26,27, 30, 31]
# list3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28,29, 30, 31]
# list4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27,28, 29, 30, 31]
# list5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27, 28, 29, 30, 31]
# sumFirstDay=0
# for i in range(5):
#     realDay=input()
#     if realDay=='true' and i==0:
#         sumFirstDay+=list1[0]
#     if realDay=='true' and i==1:
#         sumFirstDay+=list2[0]
#     if realDay=='true' and i==2:
#         sumFirstDay+=list3[0]
#     if realDay=="true" and i==3:
#         sumFirstDay+=list4[0]
#     if realDay=="true" and i==4:
#         sumFirstDay+=list5[0]
# if sumFirstDay==0:
#     sumFirstDay="There are not the day of their born"
# print(sumFirstDay)

# ------- fontion -------------

# def sumOffirstIndex(list1,list2,list3,list4,list5):
#     sumRealFirst=0
#     for i in range(5):
#         realDay=input()
#         if realDay=="true" and i==0:
#             sumRealFirst+=list1[0]
#         if realDay=='true' and i==1:
#             sumRealFirst+=list2[0]
#         if realDay=="true" and i==2:
#             sumRealFirst+=list3[0]
#         if realDay=="true" and i==3:
#             sumRealFirst+=list4[0]
#         if realDay=='true' and i==4:
#             sumRealFirst+=list5[0]
#     return sumRealFirst
# list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25,27, 29, 31]
# list2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26,27, 30, 31]
# list3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28,29, 30, 31]
# list4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27,28, 29, 30, 31]
# list5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27, 28, 29, 30, 31]
# totalResult=sumOffirstIndex(list1, list2, list3, list4, list5)
# if totalResult==0:
#     totalResult="there are not day of born"
# print(totalResult)



#3

# potionOfHarry=input()
# isReal=False
# numOfpotion=0
# countLife=2
# for i in range(len(potionOfHarry)):
#     if potionOfHarry[i]=="H":
#         isReal=True
#     if isReal  and potionOfHarry[i]=="V":
#         countLife-=1
#     if (countLife==0 and isReal) or ((i == len(potionOfHarry)-1) and isReal):
#         isReal=False
#         print(i)
#     if potionOfHarry[i]=="P":
#         countLife+=1

    



# --------- Holloween 2 ---------
#1

# gridSquare=eval(input())
# for row in range(len(gridSquare)):
#     sumOfrow=0
#     sumOfcol=0
#     isSquare=False
#     for col in range(len(gridSquare[row])):
#         sumOfrow+=gridSquare[col][row]
#         sumOfcol+=gridSquare[row][col]
#     if sumOfcol==sumOfrow:
#         isSquare=True
# message="This is not a magic square" + "\n" + str(gridSquare)
# if isSquare:
#     message="This is magic square" +"\n" + str(gridSquare)
# print(message)
        
# ------ fontion ----------

# def gridSquare(arraySquare):
#     for row in range(len(arraySquare)):
#         sumRow=0
#         sumCol=0
#         isSquare=False
#         for col in range(len(arraySquare)):
#             sumRow+=arraySquare[col][row]
#             sumCol+=arraySquare[row][col]
#         if sumRow==sumCol:
#             isSquare=True
#     return isSquare
# arraySquare=eval(input())
# message="This is not a magic square" + "\n" + str(gridSquare)
# if gridSquare(arraySquare):
#     message="This is magic square" +"\n" + str(gridSquare)
# print(message)

#2

# star=""
# N=int(input())
# for row in range(N):
#     star+=" "*(N-row) + "* "*(row+1) +"\n"
# print(star)

# --------- fontion -----------

# def getParamit(n):
#     star=""
#     for p in range(n):
#         star+=" "*(n-p) + "* "*(p+1) + "\n"
#     return star
# n=int(input())
# print(getParamit(n))

#3

# moveD=eval(input())
# founD=False
# moveChar=input()
# row=0
# col=0
# for y in range(len(moveD)):
#     for x in range(len(moveD[y])):
#         if moveD[y][x]=="D":
#             row=y
#             col=x
#             founD=True
# if founD:
#     if moveChar=="L" and col!=0:
#         moveD[row][col-1]="D"
#         moveD[row][col]=0
#     if moveChar=="R" and col<(len(moveD[0])-1):
#         moveD[row][col+1]="D"
#         moveD[row][col]=0
#     if moveChar=="D" and row<(len(moveD)-1):
#         moveD[row+1][col]="D"
#         moveD[row][col]=0
#     if moveChar=="U" and row!=0:
#         moveD[row-1][col]="D"
#         moveD[row][col]=0
# print(moveD)

# ---------- foction ---------

# def findingCharD(grid):
#     y=0
#     x=0
#     foundCharD=False
#     for row in range(len(grid)):
#         for col in range(len(grid[row])):
#             if grid[row][col]=="D":
#                 y=row 
#                 x=col
#                 foundCharD=True
#     if foundCharD:
#         if charMove=="L" and x!=0:
#             grid[y][x-1]="D"
#             grid[y][x]=0
#         if charMove=="R" and x<(len(grid[0])-1):
#             grid[y][x+1]="D"
#             grid[y][x]=0
#         if charMove=="D" and y<(len(grid)-1):
#             grid[y+1][x]="D"
#             grid[y][x]=0
#         if charMove=="U" and y!=0:
#             grid[y-1][x]="D"
#             grid[y][x]=0
#     return grid
# charMove=input()
# grid=eval(input())
# print(findingCharD(grid))


# ------ Warmpire ---------
