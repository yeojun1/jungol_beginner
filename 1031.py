board=[]
nums=[]
tmp=[]
isBingo=0
bingoCnt=0
cnt=0

# 빙고판 입력
for _ in range(5):
    board.append(list(map(int, input().split())))

# 부른 수 입력
for _ in range(5):
    tmp = list(map(int, input().split()))
    nums.extend(tmp)

def check():
    global board, bingoCnt
    bingoCnt = 0  # 매 호출 전에 초기화
   
    # 가로 체크
    for y in range(5):
        if all(board[y][x] == 0 for x in range(5)):
            bingoCnt += 1
   
    # 세로 체크
    for x in range(5):
        if all(board[y][x] == 0 for y in range(5)):
            bingoCnt += 1

    # 대각선 체크
    if all(board[j][j] == 0 for j in range(5)):
        bingoCnt += 1
    if all(board[4 - j][j] == 0 for j in range(5)):
        bingoCnt += 1

# 빙고 확인
for i in range(25):
    for a in range(5):
        for b in range(5):
            if board[a][b] == nums[i]:  # 수를 찾으면
                board[a][b] = 0
                cnt += 1

    if cnt >= 12:
        check()
        # 빙고가 3개 이상 되면
        if bingoCnt >= 3:
            break

# 최종 카운트 출력
print(cnt)

# # board=빙고판, nums=부른 수, tmp=부른 수 format 임시 리스트, isBingo=빙고 여부 판단용 변수, bingoCnt=빙고 갯수 셈 cnt=출력값(몇번만에 빙고인지)
# board=[]
# nums=[]
# tmp=[]
# isBingo=0
# bingoCnt=0
# cnt=0
# # 빙고판 입력
# for _ in range(5):
#     board.append(list(map(int,input().split())))

# # 부른 수 입력
# for _ in range(5):
#     tmp=list(map(int,input().split()))
#     for n in range(5):
#         nums.append(tmp[n])

# def check():
#     global board,nums,isBingo,bingoCnt,cnt
#     for y in range(5):
#         isBingo=0
#         for x in range(5):
#             if board[y][x]==0:
#                 isBingo+=1
#         if isBingo==5:
#             bingoCnt+=1
    
#     for y in range(5):
#         isBingo=0
#         for x in range(5):
#             if board[x][y]==0:
#                 isBingo+=1
#         if isBingo==5:
#             bingoCnt+=1
    
#     isBingo=0
#     for j in range(5):
#         if board[j][j]==0:
#             isBingo+=1
#     if isBingo==5:
#         bingoCnt+=1
    
#     isBingo=0
#     for j in range(5):
#         if board[4-j][j]==0:
#             isBingo+=1
#     if isBingo==5:
#         bingoCnt+=1

# # 빙고 확인
# for i in range(25):
#     cnt+=1
#     # 부른 수 빙고 보드에서 0으로 변경
#     for a in range(5):
#         for b in range(5):
#             try:
#                 idx=board[a].index(nums[i])
#             except ValueError: continue
#             board[a][idx]=0
#     if cnt>=12:
#         check()
#         # 빙고가 3개 이상 되면
#         if bingoCnt>=3:
#             # for문 중단
#             break
# # 위에서 정의한 cnt 출력
# print(cnt)