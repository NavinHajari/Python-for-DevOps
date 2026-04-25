a = 70
b = 60
c = 60

def check_biggest(a, b, c):

    if a > b and a > c:
        print(" A is the biggest")
    elif b > a and b > c:
        print("B is the biggest")
    elif c > a and c > b:
        print("C is the biggest")
    else:
        print(" All are equal")

a = input("Input a")
b = input("Input b")
c = input("Input c")
check_biggest(a, b, c)
    