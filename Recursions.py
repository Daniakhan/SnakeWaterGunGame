# def print2(str1):
#     print("This is " + str1)
# print2("Dania")

def factorial_iterative(n):
    """
    :param n: integer
    :return: n * n-1 * n-2 * n-3 * .. 1
    """
    fac = 1
    for i in range(n): # 0 - (n-1):
        fac = fac * (i+1)
    return fac
def factorial_recursive(n):
    """
    :param n: integer
    :return: n * n-1 * n-2 * n-3 * .. 1
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


def fibbonacci (n):
    if n ==1: #position
        return 0
    elif n==2: #position
        return 1
    return fibbonacci(n-1) + fibbonacci(n-2)
number = int(input("Enter the number: "))
# print("Factorial using iterative method: ",factorial_iterative(number))
# print("Factorial using recursive method: ",factorial_recursive(number))
print(fibbonacci(number))