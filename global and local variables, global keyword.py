l = 10 # global variable
def function1(n):
    l = 5 #local
    m = 8 # local
    global l
    l= l + 50
    print(l, m)
    print(n, "I have printed")

function1("This is me")
print(m)

def harry():
    x = 20
    def rohan():
        global x
        x = 88
        print("before calling rohan()",x)
        rohan()
        print("after calling rohan()", x)
harry()

Quiz#

