T = int(input())


def count_one(string):
    N = len(string)
    count = 0
    for i in range(N):
        if string[i]=='1':
            count+=1
    return count


for _ in range(T):
    N = int(input())
    string = input()
    count = count_one(string)
    print(count*(count+1)//2)
