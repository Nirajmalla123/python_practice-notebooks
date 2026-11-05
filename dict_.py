# # """
# # indexing,order,multiple data, duplicated ,mutable,not duplicate key
# # {key:value}

# # """
# # d={}
# # print(type(d))
# # e=dict()
# # print(type(e))

# a={'a':'Apple','b':'Ball'}
# print(a)
# print(a['a'])
# a={'a':'Apple','b':'Ball','b':'Apple'}
# print(a)

# a={}
# a.update({'a':10})
# print(a)

# # #update value
# # a['a']=20
# # print(a)

# #Update key
# a['ab']=a.pop('a')
# print(a)

# #delete value
# del a['ab']
# print(a)

# ###WAP to input 'n' peoples names and phone numbers and store them in a dictionary.Finally ,display the dictionary.

# n = int(input("Enter how many names: "))

# detail = {}
# for i in range(n) :
#     name=input("Enter your name:")
#     phone=int(input("Enter your phone number"))
#     detail[name]=phone
# print(detail)

# #or other way to solve 
# info={}
# n=int(input("Enter n="))
# for i in range(n):
#     name=input("Enter name:")
#     phone=int(input("Enter phone number:"))
#     info.update({name:phone})
# print(info)


# #only key
# for i in info:
#     print(i)

# #only values
# for i in info.values():
#     print(i)


# b=[['1',10],['2',20],['3',30]]
# print(dict(b))


# info=()
# n=int(input("Enter n="))
# for i in range(n):
#     name=input("Enter name=")
#     phone=input("Enter phone=")
#     phone2=input("Enetr phone2=")
#     info.update({name:[phone,phone2]})
# print(info)

# #{'ram':['98687','98667'],'hari':['2345','6545']}
# info={'name':[],'phone':[]}
# n=int(input("enter n="))
# for i in range(n):
#     name=input("Enter name=")
#     phone=input("enter phone=")
#     info['name'].append(name)
#     info['phone'].append(phone)
# print(info)

#WAP to store multiple users name ,adddress,age and one or more phone numbers in a dictionary and display all the stored data at the end
# info={'name':[],'phone':[],'phone2':[],'address':[],'age':[]}
# n=int((input("Enter n=")))
# for i in range(n):
#     name=input("Enter name=")
#     age=int(input("Enter age="))
#     phone=input("Enter phone=")
#     phone2=input("Enter phone2=")
#     address=input("Enter address=")
#     if phone2.lower=='y':
#         phone+=input("Enter additional phone number seperated by space:").split()
#     info['name'].append(name)
#     info['phone'].append(phone)
#     info['age'].append(age)
#     info['address'].append(address)
# print(info)

# #WAP to increase each employees salary by 10% and print the updated dictionary
# emp={}
# n=int(input("Enter n="))
# for i in range(n):
#     name=input("enter your name:")
#     salary=int(input("Enter salary="))
#     emp[name]=salary*0.1+salary
# print(emp)


# #WAp to sort students by their marks in ascending order and print the result

# student={}
# n=int(input("Enter n="))
# for i in range(n):
#     name=input("Enter name=")
#     marks=int(input("Enter marks="))
#     student[name]=marks
# sorted_student=dict(sorted(student.items(),key=lambda x:x[1]))
# print(sorted_student)

# #emp={'Ram':10000,'Sita':30000}

# student={'ram':10000,'sita':30000}
# for i in student:
#     student[i]=student[i]*0.1+student[i]
# print(student)

#or
# student={'ram':10000,'sita':30000}
# data={i:int(k*1.10) for i,k in student.items()}
# print(data)

#Sort name and marks according to accending order
students={'RAm':54,"Sita":34,"Hari":89}
marks= list(students.values())
marks.sort()
for i in marks:
    for name in students:
        if(students[name]==i):
            print({name:i})

