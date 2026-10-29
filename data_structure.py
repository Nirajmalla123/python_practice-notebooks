##To search for a name in a list and display the total number of occurence(case-sensitive)
# n = int(input("Enter how many numbers: "))

# numbers = []

#  for i in range(n):
#     num = int(input("Enter a number: "))
#      numbers.append(num)

#  print("The list is:", numbers)
 

##To take n number from the user and store them in a list,then display the list
# names = ["Ram", "Sita", "ram", "Hari", "RAM", "Sita"]

# search = input("Enter the name to search: ")

# count = 0
# for name in names:
#   if name.lower() == search.lower():
#          count += 1

#  print("Total occurrences:", count)


# #to create a list of numbers and and find the second largest
n = int(input("How many numbers do you want to enter? "))

numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

numbers = list(set(numbers))
numbers.sort()

if len(numbers) >= 2:
    print("Second largest number:", numbers[-2])
else:
    print("Second largest number does not exist.")
