

# a=[[2,3,4],[7,8,9]]
# print(a[1])


#1

# a=[[1,7,3,4],[5,6,7,8],[9,1,1,1]]
# newValue=''
# for n in range(len(a[0])):
#     newValue += str(a[0][n]) + "-"
# print(newValue)

#2
# a=[[1,7,3,4],[5,6,7,8],[9,1,1,1]]
# newValue=''
# for n in range(len(a[2])):
#     newValue += str(a[2][n]) + "-"
# print(newValue)
# #3

# a=[[1,7,3,4],[5,6,7,8],[9,1,1,1]]
# newvalue=''
# for n in range(len(a)):
#     newvalue += str(a[n][3]) + "-"
# print(newvalue)

# WEEK14////////

# #1
# def equalArray(list1,list2):
#     isEqual=True
#     if len(list1)==len(list2):
#         n=0
#         for a in list1:
#             if a == list2[n]:
#                 n+=1
#                 isEqual=True
#             else:
#                 isEqual=False
#     else: 
#          isEqual=False
#     return isEqual
# list1=eval(input())
# list2=eval(input())
# equalValue=equalArray(list1, list2)
# message="NOT EQUAL"
# if equalValue:
#     message="EQUAL"
# print(message)

#2

# def splitByspace(string):
#     newArray=[]
#     for char in string:
#         newText=""
#         if char==" ":
#             if len(newText)>0:
#                 newArray.append(newText)
#         else:
#             newText += char
#     if len(newText)>0:
#         newArray.append(newText)
#     return newArray
# string = input()
# print(splitByspace(string))

# 3,We replaced all 7 by 8 and all 1 by 0 in the array 2D
#3

# def remvoeNumber(number):
#     for rows in number:
#         for cols in range(len(rows)): 
#             if rows[cols]==7:
#                 rows[cols]=8 
#     return number
# array=eval(input())
# print(remvoeNumber(array))

# inserting array to 2d array by append (object)

# numbers=[]
# numbers.append([1,2,3])
# numbers.append([4,5,6])
# print(numbers)

#2
# numbers=[]
# array=[]
# array.append(2)
# array.append(3)
# numbers.append(array)
# print(numbers)

#1
# array=eval(input())
# resultArray2d=[]
# array2d=[]
# for row in array:
#     for col in row:
#         array2d.append(col.upper())
#     resultArray2d.append(array2d)
#     array2d=[]
# print(resultArray2d)

# ...... functoin ......

# def array2D(array):
#     resultArray2d=[]
#     newArray=[]
#     for row in array:
#         for col in row:
#             newArray.append(col.upper())
#         resultArray2d.append(newArray)
#         newArray=[]
#     return resultArray2d
# array=eval(input())
# print(array2D(array))


#2
#use funtoin Max  
# array2d=eval(input())
# array=[]
# for row in array2d: 
#     array.append(max(row))
# print(array)
            
# array2d=eval(input())
# array=[]
# for row in range (len(array2d)):
#     maxNumber= array2d[row][0]
#     for col in range (len(array2d[row])):
#         if array2d[row][col]>maxNumber:
#             maxNumber = array2d[row][col]
#     array.append(maxNumber)
# print(array)

 ###### fuctoin #########

# def array(array2D):
#     newArray=[]
#     for row in range(len(array2D)):
#         maxNumber=array2D[row][0]
#         for col in range(len(array2D[row])):
#             if array2D[row][col]>maxNumber:
#                 maxNumber=array2D[row][col]
#         newArray.append(maxNumber)
#     return newArray
# array2D=eval(input())
# print(array(array2D))


#4
# array2D = eval(input())
# for row in array2D:
#     for col in range(len(row)):
#         if row[col]==7:
#             row[col]=8
# print(array2D)

###### fuctoin #########

# def remvoeNumber(number):
#     for rows in number:
#         for cols in range(len(rows)): 
#             if rows[cols]==7:
#                 rows[cols]=8 
#     return number
# array=eval(input())
# print(remvoeNumber(array))


#3
# array2d=eval(input())
# newArray=[]
# for row in range(len(array2d)):
#     for col in range (len(array2d[row])):
#         if array2d[row][col]== 7:
#             newArray.append(row)
#             newArray.append(col)
# print(newArray)

###### fuctoin #########

# def array(array2D):
#     newArray=[]
#     for row in range(len(array2D)):
#         for col in range(len(array2D[row])):
#             if array2D[row][col]==7:
#                 newArray.append(col)
#                 newArray.append(row)
#     return newArray
# array2D=eval(input())
# print(array(array2D))


#5
# array2d=eval(input())
# if len(array2d)>=3:
#     for row in array2d:
#         for col in range(len(row)):
#             row[2]="*"
# print(array2d)


# The holiday exercise my self
#1

# def sumArray2D(array2D):
#     newArray2D=[]
#     for cols in range(len(array2D[0])):
#         sumOfcols=0
#         for rows in range(len(array2D)):
#             sumOfcols+=array2D[rows][cols]
#         newArray2D.append(sumOfcols)
#     return newArray2D
# array2D=eval(input())
# print(sumArray2D(array2D))



# ------------- week2 ---------------------------
#1

# array2D=eval(input())
# newArray2D=[]
# newArray=""
# for row in array2D:
#     for col in row:
#         newArray += str(col.lower())
#     newArray2D.append(newArray)
#     newArray=""
# print(newArray2D)

# ----functoin using-----

# def combinArray(array2D):
#     newArray2D=[]
#     newArray=''
#     for row in array2D:
#         for col in row:
#             newArray += str(col.lower())
#         newArray2D.append(newArray)
#         newArray =''
#     return newArray2D
# array2D=eval(input())
# print(combinArray(array2D))


#2

# array2D=eval(input())
# newArray2D=[]
# for col in range(len(array2D[0])):
#     sumOfcolumn=0
#     for row in range(len(array2D)):
#         sumOfcolumn += array2D[row][col]
#     newArray2D.append(sumOfcolumn)
# print(newArray2D)

#-----fonctoin--------

# def sumArray2D(array2D):
#     newArray2D=[]
#     for cols in range(len(array2D[0])):
#         sumOfcols=0
#         for rows in range(len(array2D)):
#             sumOfcols+=array2D[rows][cols]
#         newArray2D.append(sumOfcols)
#     return newArray2D
# array2D=eval(input())
# print(sumArray2D(array2D))


#3

# array2D=eval(input())
# newArray2D=[]
# for col in range(len(array2D[0])):
#     minNumber=array2D[0][col]
#     for row in range(len(array2D)):
#         if array2D[row][col]<minNumber:
#             minNumber = array2D[row][col]
#     newArray2D.append(minNumber)
# print(newArray2D)


# ----functoin-----

# def minNumbers(array2D):
#     newArray2D=[]
#     for col in range(len(array2D[0])):
#         minNumber=array2D[0][col]
#         for row in range(len(array2D)):
#             if array2D[row][col] < minNumber:
#                 minNumber = array2D[row][col]
#         newArray2D.append(minNumber)
#     return newArray2D
# array2D=eval(input())
# print(minNumbers(array2D))


#4

# persons=eval(input())
# age=int(input("Enter: "))
# nameOfpersons=""
# for row in persons:
#     for col in range(len(row)):
#         if row[col]== age:
#             nameOfpersons += str(row[0]) + "\n"
# print(nameOfpersons)
        
# ------functoin-----

# def finNames(persons,age):
#     nameOfArray=''
#     for row in persons:
#         for col in range(len(row)):
#             if row[col] == age :
#                 nameOfArray += str(row[0]) + "\n"
#     return nameOfArray
# persons=eval(input())
# age=int(input())
# print(finNames(persons, age))

##### 5 #########

# array2D=[[1,7,3],[9,3,6],[4,8,5]]
# newArray2D=[]
# for col in range(len(array2D[0])):
#     minNumber=array2D[0][col]
#     for row in range(len(array2D)):
#         if array2D[row][col]<minNumber:
#             minNumber=array2D[row][col]
#     newArray2D.append(minNumber)
# print(newArray2D)


############   week3     ###########
#1

# m=[ [3, 3],  [1, 2],  [4, 0] ]
# for row in range(5):
#     rows=''
#     for col in range(5):
#         conditoin=False
#         for n in range(len(m)):
#             if col==m[n][0] and row==m[n][1]:
#                 conditoin=True
#         if conditoin:
#             rows +="*"
#         else:
#             rows +="0"
#     print(rows)

# ------ functoin ---------   

# def hasMonsterOnCell(monsterPosition,cellX,cellY):
#     hasMonster=False
#     for a in range(len(monsterPosition)):
#         if monsterPosition[a][1]== cellY and monsterPosition[a][0]==cellX:
#             hasMonster=True
#     return hasMonster
# value=eval(input())
# for cellY in range(5):
#     playMonster=""
#     for cellX in range(5):
#         if hasMonsterOnCell(value, cellX, cellY):
#             playMonster +="*"
#         else:
#             playMonster+="0"
#     print(playMonster)


#2

# array2D=eval(input())
# newArray2D=[]
# for row in array2D:
#     countOddRow=0
#     for col in row:
#         if col%2==1:
#             countOddRow+=1
#     newArray2D.append(countOddRow)
# print(newArray2D)

#3
# array2D=eval(input())
# newArray=[]
# for col in range(len(array2D[0])):
#     countCol=0
#     averageCols=0
#     for row in range(len(array2D)):
#         countCol+= array2D[row][col]
#     averageCols=int(countCol/len(array2D))
#     newArray.append(averageCols)
# print(newArray)

#4

# array2D=eval(input())
# number=int(input())
# for col in range(len(array2D[0])):
#     for row in range(len(array2D)):
#         if col == number:
#             array2D[row][col]="*"
#         elif (len(array2D)-1)<number:
#             array2D="Out of range"
# print(array2D)


    
# ------ week 4 -------

#1

# array2D=eval(input())
# number=int(input())
# for col in range(len(array2D[0])):
#     for row in range (len(array2D)):
#         array2D[row][number]="*"
# print(array2D)

# --- functoin -----------

# def replaceChar(array2D,number):
#     for col in range(len(array2D[0])):
#         for row in range(len(array2D)):
#             if len(array2D[row])-1>=number :
#                 array2D[row][number]="*"
#             else:
#                 array2D="column error"
#     return array2D
# array2D=eval(input())
# number=int(input())
# print(replaceChar(array2D, number))


#2

# ---- functoin -------

# def replaceChar(array2D,number):
#     for row in range(len(array2D)):
#         for col in range(len(array2D[row])):
#             array2D[number][col]="*"
#     return array2D
# array2D=eval(input())
# number=int(input())
# print(replaceChar(array2D, number))
       

#3

# array=eval(input())
# numberX=0
# for i in range(len(array)):
#     if array[i]=="X":
#         numberX=i
# if len(array)-1>numberX:
#     array[numberX]="0"
#     array[numberX+1]="X"
# print(array2D)

# --------- functoin ---------

# def moveXToRight(array):
#     numberX=0
#     for i in range(len(array)):
#         if array[i]=="X" :
#             numberX=i
#     if len(array)-1>numberX:
#         array[numberX]="0"
#         array[numberX+1]="X"
#     return array
# array=eval(input())
# print(moveXToRight(array))

#4

# personsInRoom=eval(input())
# newPersonrow=int(input())
# newPersoncolumn=int(input())
# numberPerson=0
# for y in range(len(personsInRoom)):
#     for x in range(len(personsInRoom[y])):
#         if personsInRoom[y][x]==1 :
#             numberPerson+=1
# if numberPerson<3:
#     if personsInRoom[newPersonrow][newPersoncolumn]== 0:
#         print("CAN ADD")
# else:
#     print("CANNOT ADD")

#1

# array2D=eval(input())
# isRow7=False
# for row in array2D:
#     number7=0
#     for col in row:
#         if col==7:
#             number7+=1
#     if number7==len(array2D[0]):
#         isRow7=True

# if isRow7:
#     print("win")
# else:
#     print("lost")

#2

# array2D=[[1,2,3],[1,2][1,2,3]]
# newArray2D=[[1,2,3],[1,2,3][1,2,3]]
# rowEqual=False
# message="not equal"
# for row in range(len(array2D)):
#     firstRow=(array2D[row])
#     newRow=(newArray2D[row])
#     for col in range(len(array2D[row])):
#         if len(array2D[row])==len(newArray2D[row]):
#             if firstRow[col]==newRow[col]:
#                 rowEqual=True
# if rowEqual:
#     message="equal"
# print(message)



# ------- review deficult Exercise week4 ---------
#1

# def hasMonsterOnCell(hasMonster,cellX,cellY):
#     realMonster=False
#     for mon in hasMonster:
#         x=mon[0]
#         y=mon[1]
#         if x==cellX and y==cellY:
#             realMonster=True
# value=eval(input())
# for Y in range(5):
#     monster=""
#     for X in range(5):
#         if hasMonsterOnCell(hasMonster, X, Y):
#             monster+="*"
#         else:
#             monster+="0"
#     print(monster)

# ---- week 5 review ------

# personsInRoom=eval(input())
# addpersonInrow=int(input())
# addpersonIncol=int(input())
# count=0
# for val in personsInRoom:
#     for v in val:
#         if val==1:
#             count+=1
# if count<3 and personsInRoom[addpersonIncol][addpersonInrow]==0:
#     print("CAN ADD")
# else:
#     print("CAN'T ADD")


# ----------------- tic tac toe gaming and grid -----------

#   @param grid   (an array 2D)
#   @param rowIndex  (integer)
#   @param sign  (string)
# #   @return True if the ROW at the given rowIndex is composed ONLY of the given sign

# def signOnRow(grid, rowIndex, sign):
#     result=False
#     countSign=0
#     for col in range(len(grid[rowIndex])):
#         if grid[rowIndex][col]==sign:
#             countSign+=1
#     if countSign==3:
#         result=True

# #   @param grid   (an array 2D)
# #   @param columnIndex  (integer)
# #   @param sign  (string)
# #   @return True if the ROW at the given columnIndex is composed ONLY of the given sign
# def signOnColumn(grid, columnIndex, sign):
#     result=False
#     countSign=0
#     for row in range(len(grid)):
#         if grid[row][columnIndex]==sign:
#             countSign+=1
#     if countSign==3:
#         result=True
#     return result

# #    @param grid   (an array 2D)
# #    @param sign  (string)
# #    @return True if a DIAGONAL is composed ONLY of the given sign
# def signOnDiagonal(grid, sign):
#     result=False
#     countDiagnolRight=0
#     for row in range(len(grid)):
#         for col in range(len(grid[row])):
#             if (col==row and grid[row][col]==sign):
#                 countDiagnolRight+=1
#     countDiagonalLeft=0
#     col=len(grid[0])
#     for row in range(len(grid)):
#         col-=1
#         if grid[row][col]==sign:
#             countDiagonalLeft+=1
#     if countDiagonalLeft==3 or countDiagnolRight==3:
#         result=True
#     return result   

# #    @param grid   (an array 2D)
# #    @param sign  (string)
# #    @return True if the given sign has WON
# def hasSignWon(grid, sign):
#     ticTacToe=False
#     for i in range(len(grid)):
#         if signOnRow(grid, i, sign) or signOnColumn(grid,i,sign) or signOnDiagonal(grid,sign):
#             ticTacToe=True
#     return ticTacToe

# #      It true if : 
# #       - one of the 2 diagonal is composed of this sign
# #       - or if 1 of the 3 rows is composed of this sign
# #       - or if 1 of the 3 columns is composed of this

    
# #  MAIN PROGRAM (nothing to change here !)

# grid = eval(input())
# if hasSignWon(grid, "A"):
#     print("A WON")

# elif hasSignWon(grid, "B"):
#     print("B WON")

# else:
#     print("NO WINNER")


# array2D=eval(input())
# newArray2D=[]
# for rows in array2D:
#     newArray=[]
#     char=""
#     for cols in rows:
#         char += cols.lower()
#     newArray.append(char)
#     newArray2D.append(newArray)
# print(newArray2D)

# ar=[['a','b'],['b','d']]
# for row in range (len(ar)):
#     char=""
#     for col in ar[row]:
#         char+=col.lower()
#     ar[row]=char
# print(ar)
        
# array2D=eval(input()) 
# foundSeven=False  
# for row in array2D:
#     countSeven=0
#     for col in row:
#         if col==7:
#             countSeven+=1
#     if countSeven==len(row):
#         foundSeven=True
# message="Lost"
# if foundSeven:
#     message="Win"
# print(message)
        
            
        
    










