t = int(input())


def infix_to_postfix(exp, n):
    stack = []
    stack_len=0
    postfix_exp = ''
    operator = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1,
        '^': 2
    }
    for i in range(n):
        if 65 <= ord(exp[i]) <= 90:
            postfix_exp+=exp[i]
        elif exp[i] == '(':
            stack.append(exp[i])
            stack_len+=1
        elif exp[i] in operator:
            if stack_len == 0 or stack[-1] == '(':
                stack.append(exp[i])
                stack_len+=1
            elif operator[exp[i]] > operator[stack[-1]]:
                stack.append(exp[i])
                stack_len+=1
            elif operator[exp[i]] <= operator[stack[-1]]:
                while stack_len > 0 and stack[-1] != '(' and operator[exp[i]] <= operator[stack[-1]]:
                    postfix_exp+=stack.pop()
                    stack_len-=1
                stack.append(exp[i])
                stack_len+=1
        elif exp[i] == ')':
            while stack_len>0 and stack[-1] != '(':
                postfix_exp+=stack.pop()
                stack_len-=1
            stack.pop()
            stack_len-=1
    if stack_len > 0:
        while stack_len > 0:
            postfix_exp+=stack.pop()
            stack_len-=1

    return postfix_exp


for _ in range(t):
    n = int(input())
    exp = input()
    print(infix_to_postfix(exp, n))
