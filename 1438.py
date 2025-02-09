area=[[0]*100 for _ in range(100)] # 100x100 사이즈의 공간 생성
for _ in range(int(input())):
    x,y=map(int, input().split()) # 왼쪽 아래 꼭짓점 위치 입력
    x-=1
    y-=1
    for i in range(x,x+10):
        for j in range(y,y+10):
            area[i][j]=1
    
    coloredArea=0 # 색칠된 영역 카운팅
    for i in area:
        for j in i:
            if j==1:
                coloredArea+=1

print(coloredArea)