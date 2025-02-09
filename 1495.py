n=int(input())
square=[[0]*n for _ in range(n)]

dx=[1,-1,0,1]
dy=[0,1,1,-1]
value=1
x,y=0,0
square[x][y]==value

for _ in range(n-1):
    for i in range(4):
        if i==0:
            value+=1
            if 0<=x+dx[0]<n and 0<=y+dy[0]<n:
                x+=dx[0]
                y+=dy[0]
                square[x][y]=value
            else:
                x+=dx[2]
                y+=dy[2]
                square[x][y]=value
        elif i==1:
            while 0<=x+dx[1]<n and 0<=y+dy[1]<n:
                value+=1
                x+=dx[1]
                y+=dy[1]
        elif i==2:
            value+=1
            if 0<=x+dx[2]<n and 0<=y+dy[2]<n:
                x+=dx[2]
                y+=dy[2]
                square[x][y]=value
            else:
                x+=dx[0]
                y+=dy[0]
                square[x][y]=value
        elif i==3:
            while 0<=x+dx[3]<n and 0<=x+dx[3]<n:
                value+=1
                x+=dx[3]
                y+=dy[3]
                square[x][y]=value

for row in square:
    print(*row)