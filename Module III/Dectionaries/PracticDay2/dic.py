# ---------- Explanation of teacher --------

# countries = {
# "khmer": 17,
# "thai" : 30,
# "vietnam": 50,
# "philipin":90
# }
# print(countries["philipin"])

#2
# menu = {}
# menu['MONDAY'] = 'rice'
# menu["TUESDAY"] = 'noodles'
# menu["MONDAY"] = 'soup'
# print(menu["MONDAY"] )


# AgeOfPopularPerson={'khey':18,'Phearun':18}
# print(AgeOfPopularPerson['khey'])

# studentsAge = { }
# studentsAge['sokan'] = 25+5
# studentsAge['sokar']=70-10
# print(studentsAge)

# studentsAge = { }
# studentsAge['sokan'] = 25
# studentsAge['seiha'] = 95
# print(studentsAge)


# food = {
# "name": "Bay Char",
# "price": 1000}
# for key in food:
#     print(key)
# for key in food:
#     print(food[key])

# studentsAge = { }
# studentsAge['sokan'] = 25
# studentsAge.pop('sokan')
# print(studentsAge)

# ---------- day1 -----------
#1
# value={"2021A": 20, "2021B": 30, "2021C": 15 }
# for key in value:
#     result=''
#     result+="Class " + str(key) + " has " + str(value[key]) +" students"
#     print(result)

#2

# value={"2021A": 20, "2021B": 30, "2021C": 15 }
# for key in value:
#     result=''
#     if key=="2021A":
#         value[key]=24
#     result+="Class " + str(key) + " has " + str(value[key]) +" students"
#     print(result)



# -------- day2-----------
#1

# studentsDictionary = eval(input())
# newStudentsNumber= int(input())
# newStudentsClass = input()
    
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# if newStudentsClass in studentsDictionary:
#    studentsDictionary[newStudentsClass]+= newStudentsNumber
# else:
#     studentsDictionary[newStudentsClass]=newStudentsNumber
# for key in studentsDictionary:
#     result=""
#     result+="Class "+str(key)+" has "+str(studentsDictionary[key])+" students"
#     print(result)


# #2
# studentsDic1 = eval(input())
# studentsDic2 = eval(input())
# result={}
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# for key1 in studentsDic1:
#     if key1 in studentsDic2:
#         result[key1]=studentsDic2[key1]+studentsDic1[key1]
#     else:
#         result[key1]=studentsDic1[key1]
# for key2 in studentsDic2:
#     if key2 not in result:
#         result[key2]=studentsDic2[key2]
# print(result)


#3

# studentsDictionary = eval(input())
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# for key in studentsDictionary:
#     result=""
#     result+="Class "+str(key)+" has "+ str(studentsDictionary[key])+" students"
#     print(result)

#4
# Enter your code here. Read input from STDIN. Print output to STDOUT
# array=eval(input())
# result={}
# for i in range(len(array)):
#     result[array[i]]=i
# print(result)

# potion="HVV0"
# charV=False
# potionV=0
# potionChar=0
# for i in range(len(potion)):
#     if potion[i].upper()=="V":
#         potionV=i
#         charV=True
#     else:
#         potionChar=i
# if charV:
#     print(potionV)
# else:
#     print(potionChar)
        