def count_primes(x,y):
    if x<2: x=2
    sieve=[True]*(y+1)
    sieve[0]=sieve[1]=False
    for i in range(2,int(y**0.5)+1):
        if sieve[i]:
            for j in range(i*i,y+1,i):
                sieve[j]=False
    return sum(sieve[x:y+1])

N=list(map(int,input().split()))
print(count_primes(N[0],N[1]))
