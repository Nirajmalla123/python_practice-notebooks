## for looop 

# syntax 

# for i in range(init,condition,in/dec):
#     print("%d",i)

x = int(input("Enter the number for table:"))

# for i in range(1, 11):
#     print(f"{x} x {i} = {x * i}")
 

# while loop
# syntax

# init

# while <Condition>:
#     <operation>
#     <inc/dec>


i = 1
while i <=10:
    print(f"{x} x {i} = {x* i}")
    i =i +1


# WAP to take balance 1000, input n times money,, subtract each time and show new balance.

# balance = 1000
# n = int(input("Enter the number of times you want to withdraw money:"))
# i = 1
# while i <= n:
#     money = int(input("Enter the amount of money you want to withdraw:"))
#     if money <= balance:
#         balance -= money
        
#         print(f"Withdrawal successful. New balance: {balance}")
#     else:
#         print("Insufficient balance.")
#         i += 1


# wap to take n inputs of text and display all entered texts together.

n = int(input("Enter the number of texts you want to input:"))
texts = []
for i in range(n):
    text = input(f"Enter text {i + 1}: ")
    texts.append(text)
print(f"You entered: {', '.join(texts)}")   

# name = input("Enter the number of texts you want to input:")
# address = input("Enter the number of texts you want to input:")
# hobby = input("Enter the number of texts you want to input:")
# study = input("Enter the number of texts you want to input:")

# print(f"my name is {name}, my address is {address}, my hobby is {hobby}, and I study {study}.")
