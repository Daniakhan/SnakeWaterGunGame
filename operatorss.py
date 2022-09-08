"""Operators
Arithmetic, assignment, logical, bitwise, membership, identity, comparison"""

#Arithmetic operators
print("5+6 is", 5+6)
print("55//6 is", 55//6)#We will receive answer without decimal / Floor
print("2**3 is", 2**3) #exponential
print("13%6 is", 13%6)#modulas

#Assignment operators
x= 5
print(x)
x+=9
print(x)

#comparison operators
i= 3
print(i==5)

#Logical operators = Boolean algebra
a = True
b = False
print(a or b)

#Identity operators
print(a is b)
print (a is not b)

#Membership operators
list = [1,2,3]
print(3 in list)
print(1 not in list)

#Bitwise operators
print(0 & 1) #and
print(0 | 1) #or
print(0 | 3)
