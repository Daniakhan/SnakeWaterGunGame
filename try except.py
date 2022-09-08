a = input("Enter first number.")
b = input("Enter second number")
try:
    print("Sum of two numbers",
          int(a) + int(b))
except Exception as e:
    print(e)

print("This line is important")
