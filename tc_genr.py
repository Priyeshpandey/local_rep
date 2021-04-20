import random as rnd
with open('input.txt', 'w') as file:
    t=input('Enter number of TCs: ')
    file.write(t+'\n')
    for i in range(int(t)):
        str_len = rnd.randint(1,10)
        file.write(str(str_len)+'\n')
        inp_str = ''
        for n in range(str_len):
            inp_str+=f'{rnd.randint(1,10)} '
        file.write(inp_str+'\n')