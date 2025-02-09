N,M=map(int,input().split())


arr = [0] * 101
result = []

def dice(step, sum_):
    if step > N:
        if sum_==M:
            result.append(" ".join(map(str, arr[1:N+1])))
        return
    
    for i in range(1, 7):
        arr[step]=i
        dice(step+1, sum_+i)

dice(1,0)
print("\n".join(result))