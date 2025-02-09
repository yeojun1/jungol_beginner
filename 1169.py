import itertools as it

N,M=map(int,input().split())

match M:
    case 1:
        res=list(it.product('123456', repeat=N))
        for i in range(len(res)):
            print(*res[i])
    case 2:
        res=list(it.combinations_with_replacement('123456', N))
        for i in range(len(res)):
            print(*res[i])
    case 3:
        res=list(it.permutations('123456',N))
        for i in range(len(res)):
            print(*res[i])