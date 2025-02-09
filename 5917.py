N,T=map(int,input().split())
x,y,z=list(range(1,N+1)),[],[]
x.reverse()

for _ in range(T):
    C,D=map(int,input().split())
    if C==1:
        for _ in range(D):
            y.append(x[-1])
            x.pop(-1)
    else:
        for _ in range(D):
            z.append(y[-1])
            y.pop(-1)
z.reverse()

for i in range(N):
    print(z[i])