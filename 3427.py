n=int(input())
balls=list(input())
cnt=[0]*4
cntB=balls.count("B")
cntR=balls.count("R")

for i in balls:
    if i=="B":
        cnt[0]+=1
    else:
        break

for i in reversed(balls):
    if i=="B":
        cnt[1]+=1
    else:
        break

for i in balls:
    if i=="R":
        cnt[2]+=1
    else:
        break

for i in reversed(balls):
    if i=="R":
        cnt[3]+=1
    else:
        break

res=0
if cntB-max(cnt[0], cnt[1])>cntR:
    res=cntR-max(cnt[2], cnt[3])
elif cntR - max(cnt[2], cnt[3])>cntB:
    res=cntB-max(cnt[0],cnt[1])
else:
    res=min(cntB-max(cnt[0],cnt[1]), cntR-max(cnt[2],cnt[3]))

print(res)