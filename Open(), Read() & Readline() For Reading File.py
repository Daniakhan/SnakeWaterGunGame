# f = open("dania.txt", "rb")
# content = f.read()
# print(content)
#
# f.close()

f = open("dania.txt", "rt")
#content = f.read(100) #jab hum .read karenge to file pointer pura read karke khali hojayega.
#phir hum jo iterate karenge woh perform nahi hoga. Hamen line by line print karna hai.
# for line in f:
#     print(line, end="")
#print(content)


# content = f.read(100)
# print("2", content)

# #we can also use readline function to print single line
# print(f.readline())
# print(f.readline())
# print(f.readlines()) #this can also be used.

f.close()
f = open("dania.txt")
f.seek(0) # to reset pointer's position
print(f.tell()) #to know pointer's position
print(f.readline())

f.close()
