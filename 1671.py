n = int(input())

area = [[False for _ in range(101)] for _ in range(101)]

for _ in range(n):
    st_j, st_i = map(int, input().split())

    for i in range(st_i, st_i + 10):
        for j in range(st_j, st_j + 10):
            area[i][j] = True

total = 0
for j in range(1, 101):
    for i in range(1, 101):
        if area[i][j] != area[i - 1][j]:
            total += 1

for i in range(1, 101):
    for j in range(1, 101):
        if area[i][j] != area[i][j - 1]:
            total += 1

print(total)