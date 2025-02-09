def toB(S,A,B):
    num=int(S,A)
    if B==10:
        print(num)
        return
    if S=='0':
        print(0)
        return
    result=''
    q=num
    r=0
    while 1:
        r=q%B
        q//=B
        if r>=10:
            result+=chr(ord('A')+(r-10))
            continue
        result+=str(r)
        if q==0:
            break
    result=result[::-1]
    if result[0]=="0":
        print(result[1:])
    else:
        print(result)


while 1:
    ASB=input()
    if not ' ' in ASB:
        break
    a,s,b=ASB.split()
    toB(s,int(a),int(b))