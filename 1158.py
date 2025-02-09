n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    print(*arr)