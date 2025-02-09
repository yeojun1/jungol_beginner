D, K = map(int, input().split())

for A in range(1, K):
    for B in range(A, K):
        F = [0] * (D + 1)
        F[1] = A
        F[2] = B
        
        for n in range(3, D + 1):
            F[n] = F[n-1] + F[n-2]
        
        if F[D] == K:
            print(A)
            print(B)
            break
    else:
        continue
    break
