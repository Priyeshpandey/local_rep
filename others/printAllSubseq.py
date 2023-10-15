# https://www.geeksforgeeks.org/print-subsequences-string/

def printSubSeq(inp,out):
    if len(inp) == 0:
        print(out, end=' ')
        return

    printSubSeq(inp[1:], out+inp[0])
    printSubSeq(inp[1:], out)



if __name__=='__main__':
    printSubSeq('abc','')