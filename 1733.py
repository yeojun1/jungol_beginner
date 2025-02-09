answer = 0

def check(fx, fy, fcol):
    global answer
    dx = [0, 1, -1, 1]
    dy = [1, 1, 1, 0]

    for i in range(4):
        bx = fx - dx[i]
        by = fy - dy[i]
        cnt = 1
        if not (0 <= bx < 19 and 0 <= by < 19 and arr[bx][by] == fcol):
            nx = fx + dx[i]
            ny = fy + dy[i]

            while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == fcol:
                cnt += 1
                nx += dx[i]
                ny += dy[i]

        if cnt == 5:
            answer = fcol
            return

arr = [list(map(int, input().split())) for _ in range(19)]
flg = 1

for j in range(19):
    for k in range(19):
        answer = 0
        if arr[j][k] == 1 or arr[j][k] == 2:
            check(j, k, arr[j][k])

        if answer != 0:
            flg = 0
            print(answer)
            print(j + 1, k + 1)
            break
    if flg == 0:
        break

if flg == 1:
    print(0)
