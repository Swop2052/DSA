# check +ve,-ve or zero 
# Write a Python program that takes an integer as input and prints:

# num = int(input("Enter NO:" ))
# if num > 0:
#     print("+ve")
# elif num < 0:
#     print("-ve")
# else:
#     print("zero")

# print(num)



# Write a Python program that takes an integer as input and checks whether it is:

# num = int(input("Enter NO:" ))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# print(num)


# Find the Greatest of Two Numbers
'''Write a Python program that accepts two numbers from the user and prints:
The greater number, or
A message saying both numbers are equal.'''

# num_1 = int(input("Enter NO:" ))
# num_2 = int(input("Enter NO:" )) 
# if num_1 > num_2:
#     print("Num1")
# elif num_2 > num_1:
#     print(num_2)
# else:
#     print("equal")


'''Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
# l = []
# for i in range(200,3201):
#     if(i%7==0) and (i%5!=0):
#         l.append(str(i))
# print(','.join(l))



# Write a Python program that accepts a number from the user and checks whether it is divisible by 5.

# num = int(input("Enter No:"))
# if num % 5 == 0:
#     print("yes")
# else:
#     print("No")


# Check Whether a Number is Divisible by Both 3 and 5
num = int(input("Enter No:"))
if num % 5 == 0 and num % 3 == 0:
    print("Y")
else:
    print("N")
