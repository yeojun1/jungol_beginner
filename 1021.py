N=int(input())
M=int(input())
ans=[0]*N
midGuide=[]
midComponent=[]
for _ in range(M):
    X,Y,K=map(int,input().split())
    midComponent.append(X)
    midGuide.append((X,Y,K))
midGuide.sort()

def addPart(part, cnt, a):
    if part not in midComponent:
        ans[part-1]+=cnt*a
        return
    for i in range(M):
        if midGuide[i][0]==part:
            addPart(midGuide[i][1], midGuide[i][2], cnt*a)

for j in range(M):
    if midGuide[j][0]==N:
        addPart(midGuide[j][1], midGuide[j][2], 1)

for idx,k in enumerate(ans,start=1):
    if k==0: continue
    print(idx,k)