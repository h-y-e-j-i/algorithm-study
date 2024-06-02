import sys

while True:
    lines = sys.stdin.readline().split(" ")
    sides = list()
    for l in lines:
        sides.append(int(l))
    sides = sorted(sides)
    side1, side2, side3 = sides[0], sides[1], sides[2]

    if side1 == 0 and side2 == 0 and side3 == 0:
        break
    elif side1 == side2 and side2 == side3 and side3 == side1:
        print("Equilateral")
    elif side1 + side2 <= side3:
        print("Invalid")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("Isosceles")
    else:
        print("Scalene")