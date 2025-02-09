from collections import Counter

while 1:
    inp=input().split()
    if inp==['END']:
        break
    sortedCNT=sorted(Counter(inp).items(), key=lambda x: x[0])
    for i in sortedCNT:
        print(f'{i[0]} : {i[1]}')