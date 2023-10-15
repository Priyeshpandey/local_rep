t = int(input())


def get_remainder(start, rem):
    rd = {
        0: 0,
        1: start,
        2: (start*10+(2*start)%10)%3,
        3: (start*1000+ 100*((2*start)%10) + (4*start)%10)%3
    }
    return rd[rem]


for _ in range(t):
    k, d0, d1 = map(int, input().split())
    d2 = (d0+d1)%10
    d3 = (2*d2)%10
    sum = -1
    if k==2:
        sum = (d0+d1)%3
    elif d2==0 or d3==0:
        sum = (d0+d1+d2+d3)%3
    else:
        k_rem = (k-3)%4
        k_val = ((k-3-k_rem)//4)*((8*d3)%10 + (4*d3)%10 + (6*d3)%10 + (2*d3)%10)%3
        val_rem = get_remainder(d3,k_rem)
        sum = (d0+d1+d2+k_val+val_rem)%3
    if sum==0:
        print('YES')
    else:
        print('NO')
# def num_genr(a, b, k):
#     sum = 10 * a + b
#     a,b=b,(a+b)%10
#     sum = sum*10+b
#     for _ in range(k):
#         a, b = b, (2*b) % 10
#         sum = sum * 10 + b
#     return sum
#
#
# for i in range(1, 10):
#     for j in range(10):
#         print(num_genr(i, j, 17))

