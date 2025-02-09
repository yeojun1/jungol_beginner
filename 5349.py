inp=input().split()
ret=[]

for i in range(len(inp)):
    if i%2==1:
        ret.append(inp[i])

for p in ret[::-1]:
    print(p,end=' ')