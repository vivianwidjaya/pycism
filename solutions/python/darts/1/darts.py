def score(x, y):
    points = 0
    distance_from_centre = (x ** 2 + y ** 2) ** 0.5
    if 0 <= distance_from_centre <= 1:
        points += 10
    elif 1 < distance_from_centre <= 5:
        points += 5
    elif 5 < distance_from_centre <= 10:
        points += 1
    else:
        points += 0
    return points
