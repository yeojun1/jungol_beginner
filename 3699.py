for _ in range(int(input())):
    Dclothes={}
    Lclothes=[]
    for _ in range(int(input())): # input을 [(hat,headgear),(sunglasses,eyeglasses)] 형식으로 저장
        A,B=input().split()
        Lclothes.append((A,B))
    
    for i in range(len(Lclothes)): # [i][1]은 i번째 의상의 종류(headgear, etc.)를 나타냄
        if Lclothes[i][1] in Dclothes: # 의상의 종류가 Dict에 있다면
            Dclothes[Lclothes[i][1]]+=1
        else:
            Dclothes[Lclothes[i][1]]=2 # 사용하지 않을 때도 포함하기 위해
    
    days=1
    for j in Dclothes.values(): # 지금까지 있었던 모든 값 더하기
        days*=j
    print(days-1) # 아무것도 입지 않을 때를 제외한 일수 출력