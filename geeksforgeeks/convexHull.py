from functools import cmp_to_key
from functools import partial


# Convex Hull using Graham's scan
def getMinY(Points) -> tuple:
    idx = 0
    for i in range(len(Points)):
        if Points[i][1] < Points[idx][1]:
            idx = i

    return Points[idx]


def compare_by_angle(A, B, refPoint):
    ax, ay = A
    bx, by = B
    x, y = refPoint

    res = (ax - x) * (by - y) - (bx - x) * (ay - y)
    if res > 0:
        return 1
    elif res == 0:
        if A == refPoint or B == refPoint or A == B:
            return 0
        else:
            OA = (ax - x) * (ax - x) + (ay - y) * (ay - y)
            OB = (bx - x) * (bx - x) + (by - y) * (by - y)
            if OA < OB:
                return -1
            elif OA == OB:
                return 0
            else:
                return 1

    else:
        return -1


def erectFence(Points: list):
    # get point with least Y coordinate
    refPoint = getMinY(Points)
    print('ref :', refPoint)
    # sort Points wrt angle it makes with refPoint
    compare_by_angle_ref = partial(compare_by_angle, refPoint=refPoint)
    Points.sort(key=cmp_to_key(compare_by_angle_ref))
    print(Points)

    stack = [refPoint, Points[1]]
    n = len(Points)
    for i in range(2, n):
        angle = compare_by_angle(A=stack[-1], B=Points[i], refPoint=stack[-2])
        print(f'RefPoint: {stack[-2]}, A: {stack[-1]}, B: {Points[i]}')
        print('Angle: ', angle)
        if angle == -1:
            stack.pop()
        stack.append(Points[i])
        print(stack)

    return stack


if __name__ == '__main__':
    points = [
        (1, 2), (2, 3), (9, 1), (0, 4), (5, 5),
        (1, 4), (3, 2), (2, 0), (4, 3), (4, 2)
    ]
    fence = erectFence(points)
