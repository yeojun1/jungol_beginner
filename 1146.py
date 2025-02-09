N = int(input())
arr = list(map(int, input().split()))

for i in range(N - 1):
    mi_index = i + arr[i:].index(min(arr[i:]))
    arr[i], arr[mi_index] = arr[mi_index], arr[i]
    for j in range(N):
        print(arr[j], end=" ")
    print()
