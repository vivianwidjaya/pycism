def equilateral(sides):
    return sides[0] == sides[1] == sides[2] and sides[0] != 0

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == b and a + b >= c:
        return True
    if a == c and a + c >= b:
        return True
    if b == c and b + c >= a:
        return True
    return False

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a + b >= c and a + c >= b and b + c >= a and a != b and a!= c and b != c
