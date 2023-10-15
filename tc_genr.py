import random as rnd
with open('input.txt', 'w') as file:
    Y = 500
    X = 100000
    t=input('Enter number of points: ')
    file.write(t+'\n')
    for i in range(int(t)):
        x = rnd.randint(0, X)
        y = rnd.randint(0, Y)
        file.write(f'{x} {y}\n')