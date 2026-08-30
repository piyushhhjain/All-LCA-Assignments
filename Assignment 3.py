def check_right_triangle(a, b, c):
    if a > b and a > c:
        hypotenuse = a
        perpendicular = b
        base = c
    elif b > a and b > c:
        hypotenuse = b
        perpendicular = a
        base = c
    else:
        hypotenuse = c
        perpendicular = a
        base = b
    if perpendicular**2 + base**2 == hypotenuse**2:
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")


a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

check_right_triangle(,,)
