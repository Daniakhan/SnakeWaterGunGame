# F strings
import math
me = "Harry"
a1 = 3
# a = "this is %s %s"%(me, a1)
# print(a)

# OR
# a = "This is {0} {0}"
# b = a.format(a1, me) #a1 is at 0 position, me at 1 position
# print(b)

a = f"this is {me} , {a1} , {4*65} , {math.cos(65)}"
print(a)

#explore time module