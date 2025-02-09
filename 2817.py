from itertools import combinations
inp=list(map(int,input().split()[1:]))
for i in combinations(inp,6):
    for j in range(6):
        print(i[j],end=" ")
    print()