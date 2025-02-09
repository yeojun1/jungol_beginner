inp=float(input())
b=inp-int(inp)
Bin=[]

for _ in range(4):
    b*=2
    if b==1.0:
        Bin.append('1')
        break
    elif b>1.0:
        Bin.append('1')
        b-=1.0
    else:
        Bin.append('0')

while len(Bin)<4:
    Bin.append('0')
print(str(bin(int(inp)))[2:],'.',''.join(Bin),sep='')
# int(inp)(정수)를 이진수(bin())으로 바꾼 후 2번째 자리부터((0b)11011) 출력
# 소수점 출력
# Bin을 뒤집어 출력