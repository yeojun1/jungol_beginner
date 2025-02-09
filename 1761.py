from itertools import permutations

def check(now_number):
    global number,strike,ball # 함수 내에서 now_number과 number,strike,ball을 비교하기 위해 global 사용
    for i in range(len(number)): # 입력받은 전체 수를 비교하는 for문 돌림
        is_strike=0 # 각각 스트라이크,볼 갯수 저장
        is_ball=0
        for j in range(3): # 수가 3자리니까 range(3)로 각 자리 비교하는 for문 돌림
            if str(now_number[j]) == number[i][j]: # now_number의 현재 인덱스 값이 입력받은 수의 현재 인덱스 값과 같다면
                is_strike+=1 # 스트라이크 1 증가
            elif str(now_number[j]) in number[i]: # 만약 이번 인덱스가 스트라이크가 아니면서 현재 넘버에 들어가 있다면
                is_ball+=1 # 볼 1 증가
        if strike[i]!=is_strike or ball[i]!=is_ball: # 만약 입력받은 스트라이크, 볼 갯수과 계산 결과가 하나라도 다르다면 return 0
            return 0
    return 1 # 위의 조건에서 멈추지 않았다면 스트라이크, 볼 갯수가 같음. 그래서 return 1

    # 입력받은 값과 확인할 값 비교
    # 입력받은 스트라이크, 볼 갯수와 비교 시 나왔던 수가 동일하면 정답일 가능성 있음
    # 만약 하나라도 다르다면 정답일 가능성 없음
    # 함수 외부에서 count+=check(num) 돌려서 정답 가능성이 있는 수의 갯수 저장

number,strike,ball=[],[],[] # 입력받은 수,스트라이크,볼 저장한 리스트
for _ in range(int(input())):
    n,s,b=map(int,input().split())
    number.append(str(n)) # number를 index로 접근할 수 있게 함
    strike.append(s) # 나머지는 int로 저장
    ball.append(b)

cand = list(permutations(range(1,10),3)) # 111~999 사이의 리스트 생성
count=0
for i in range(len(cand)): # permutation 리스트의 모든 값 대입
    count += check(cand[i]) # check함수 돌려서 정답 가능성 있는 수의 갯수 저장
print(count) # 출력