from math import floor


def coordinates(x1, y1, x2, y2, x3, y3, x4, y4):
    point_one = (x1, y1)
    point_two = (x2, y2)
    point_three = (x3, y3)
    point_four = (x4, y4)

    result_one = abs(x1) + abs(y1)
    result_two = abs(x2) + abs(y2)
    result_three = abs(x3) + abs(y3)
    result_four = abs(x4) + abs(y4)

    line1 = result_one + result_two
    line2 = result_three + result_four

    if line1 >= line2:
        if result_one <= result_two:
            print(f"{point_one}{point_two}")
        else:
            print(f"{point_two}{point_one}")

    if line1 < line2:
        if result_three <= result_four:
            print(f"{point_three}{point_four}")
        else:
            print(f"{point_four}{point_three}")


X1 = floor(float(input()))
Y1 = floor(float(input()))
X2 = floor(float(input()))
Y2 = floor(float(input()))
X3 = floor(float(input()))
Y3 = floor(float(input()))
X4 = floor(float(input()))
Y4 = floor(float(input()))

coordinates(X1, Y1, X2, Y2, X3, Y3, X4, Y4)


