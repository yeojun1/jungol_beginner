inp=input()
height=10

for i in range(1, len(inp)):
    if inp[i]==inp[i-1]:
        height+=5
    else:
        height+=10
print(height)