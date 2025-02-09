N=int(input())

arr=[list(range(1, N+1)),[]]
answer=[]
for _ in range(N): arr[1].append(int(input()))

def getAnswer(i):
    global answer
    if i>=N:
        answer = sorted(list(set(answer)))
        print(len(answer), *answer, sep='\n')
        return
    flag=False
    if i+1==arr[1][i]: flag=[i+1]
    else:
        if i+1 in arr[1]:
            j = arr[1].index(i+1)
            if arr[0][j] == arr[1][i]: flag=[i+1, arr[0][j]]

    if flag:
        for k in range(len(flag)): answer.append(flag[k])
    getAnswer(i+1)

getAnswer(0)