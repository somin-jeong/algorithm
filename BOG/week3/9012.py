import sys

N = int(sys.stdin.readline())

for i in range(N):
    input_str=sys.stdin.readline().strip()
    stack=[]
    flag=0
    for c in input_str:
        if c=='(':
            stack.append(c)
        else:
            if len(stack)==0:
                print('NO')
                flag=1
                break
            stack.pop()
    if flag==0:
        if len(stack)!=0:
            print('NO')
        else:
            print('YES')
