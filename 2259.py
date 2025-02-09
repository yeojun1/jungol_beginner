K=int(input())
arr=[list(map(int, input().split())) for _ in range(6)]

maxW=0; wIdx=0
maxH=0; hIdx=0

for idx, (direction, lenght) in enumerate(arr):
    if (direction==1 or direction==2) and (lenght>maxW):
        maxW=lenght
        wIdx=idx
    elif (direction==3 or direction==4) and (lenght>maxH):
        maxH=lenght
        hIdx=idx

subW=abs(arr[(hIdx-1)%6][1]-arr[(hIdx+1)%6][1])
subH=abs(arr[(wIdx-1)%6][1]-arr[(wIdx+1)%6][1])

print((maxW*maxH-subW*subH)*K)