#Lambda functions or Anonymous functions
# def add(a,b):
#     return a+b

# OR
#
# add = lambda a, b: a+b
# # print(add(5,4))
# def a_first(a):
#     return a[0] or #return a[1]
# a = [[1,14], [5,6], [8,23]]
# a.sort(key=a_first)
# print(a)

OR

a = [[1,14], [5,6], [8,23]]
a.sort(key= lambda x:x[0])
print(a)