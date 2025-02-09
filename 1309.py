inp=int(input())
ans=1
def fac(num):
    global ans
    ans*=num
    if num==1:
        print("1! = 1")
        return
    print(f"{num}! = {num} * {num-1}!")
    fac(num-1)
fac(inp)
print(ans)