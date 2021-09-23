def copyBits(num_a, num_b, left, right):
    # copy set bits in range 0<l<=r<32 and set them in num_a in range l to r
    # l is pos from LSB
    while left <= right:
        num_a = num_a | ((1 << (left - 1)) & num_b)
        left += 1

    return num_a


def divide(a, b):
    inf = float('inf')
    if b == 0:
        return inf

    # do a/b
    sign = -1 if ((a < 0) ^ (b < 0)) else 1
    a, b = abs(a), abs(b)
    count = 0
    while a >= b:
        count += 1
        a -= b
    print('Remainder is :', sign * a)

    return sign * count


def square(x):
    if x == 0:
        return 0
    if x % 2:
        return (square(x >> 1) << 2) + ((x >> 1) << 2) + 1
    else:
        return square(x >> 1) << 2


if __name__ == '__main__':
    # print(divide(10, -90))
    print(square(17))

