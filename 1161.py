N=int(input())

def hanoi(n, start, end, via):
    if n==1:
        print(f'1 : {start} -> {end}')
        return
    hanoi(n-1, start, via, end)
    print(f'{n} : {start} -> {end}')
    hanoi(n-1, via, end, start)


hanoi(N, 1, 3, 2)