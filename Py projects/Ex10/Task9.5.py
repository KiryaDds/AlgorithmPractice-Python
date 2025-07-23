

def take_point():
    x = float(input("x = "))
    y = float(input("y = "))
    return [x, y]


def put_point(point_list, i, point_name):
    points = dict()
    points[point_name] = point_list[i]
    return points.get(point_name)


v = take_point()
a = list(v)
print(put_point(a, 0, "A"))
