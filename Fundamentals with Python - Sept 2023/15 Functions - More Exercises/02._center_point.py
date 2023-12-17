from math import floor


def coordinates(x1, y1, x2, y2):
    point_one = (x1, y1)
    point_two = (x2, y2)

    result_one = abs(x1) + abs(y1)
    result_two = abs(x2) + abs(y2)

    if result_one <= result_two:
        return point_one
    else:
        return point_two


X1 = floor(float(input()))
Y1 = floor(float(input()))
X2 = floor(float(input()))
Y2 = floor(float(input()))

print(coordinates(X1, Y1, X2, Y2))
