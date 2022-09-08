# #Pattern printing
# Input = integer n
# Boolean variable = True or false
# True:
# *
# **
# ***
# ****
# False:
# ****
# ***
# **
# # *
num1 = int(input("Enter the number of rows:\n"))
num2 = int(input("print 0 or 1"))
new = bool(num2)
if new == True:
    for i in range(1,num1+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
elif new ==False:
    for i in range(num1,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()


#
# print("How Many Row You Want To Print")
# one= int(input())
# print("Type 1 Or 0")
# two = int(input())
# new =bool(two)
# if new == True:
#     for i in range(1,one+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif new ==False:
#     for i in range(one,0,-1):
#         for j in range(1,i+1):
#             print("*", end="")
#         print()