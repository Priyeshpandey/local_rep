

def coinChange(index, target, bag):
    if index == 0:
        return 1 if target%bag[0] == 0 else 0
    if target < 0 or index < 0:
        return 0
    if target == 0:
        return 1

    return coinChange(index, target - bag[index], bag) + coinChange(index-1, target, bag)


if __name__=='__main__':
    bag = []
    target = 10
    print(coinChange(len(bag)-1, target, bag))