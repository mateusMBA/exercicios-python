def inequality(sides):
    aux = 0
    for i in range(len(sides)):
        side = sides[i]
        sides.pop(i)
        if side > sum(sides):
            return False
        sides.insert(i,side)
    return True

def equilateral(sides):
    if inequality(sides) == False or 0 in sides:
        return False
    return sides.count(sides[0]) == 3
    


def isosceles(sides):
    if inequality(sides) == False or 0 in sides:
        return False
    for side in sides:
        if sides.count(side) >= 2:
            return True
    return False

def scalene(sides):
    if inequality(sides) == False or 0 in sides:
        return False
    for side in sides:
        if sides.count(side) >= 2:
            return False
    return True

