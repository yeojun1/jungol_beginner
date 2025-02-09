from itertools import combinations
N,K=map(int,input().split())
A=tuple(map(int,input().split()))
com=list(combinations(list(range(1,N+1)),K))
if A in com:
    print(com.index(A)+1)
else: print("None")