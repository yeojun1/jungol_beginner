cards = []
for _ in range(5):
    cards.append(''.join(input().split()).replace(' ', ''))

alphas = []
nums = []

for card in cards:
    alphas.append(card[0])
    nums.append(int(card[1]))

nums.sort()

def check():
    global nums, alphas
   
    if len(list(set(alphas))) == 1:
        if all(nums[i] == nums[0] + i for i in range(5)):
            return 900 + max(nums)
        else:
            return 600 + max(nums)

    counts = [nums.count(num) for num in set(nums)]
    if 4 in counts:
        return 800 + nums[counts.index(4)]

    if 3 in counts and 2 in counts:
        if nums.count(nums[0])==counts[0]:
            temp=counts[0]
            counts[0]==counts[1]
            counts[1]==temp
        three=0
        for i in nums:
            if nums.count(i)==3:
                three=i
                for j in range(nums.count(three)):
                    nums.remove(three)
        two = nums[counts.index(2)]
        return 700 + three * 10 + two

    if all(nums[i] == nums[0] + i for i in range(5)):
        return 500 + max(nums)

    if 3 in counts:
        return 400 + nums[counts.index(3)]

    pairs = [num for num in set(nums) if nums.count(num) == 2]
    if len(pairs) == 2:
        return 300 + max(pairs) * 10 + min(pairs)

    if 2 in counts:
        return 200 + nums[counts.index(2)]

    return 100 + max(nums)

print(check())

#  푼 방법
# cards=[]
# for _ in range(5): cards.append(''.join(input().split()).replace(' ', ''))
# alphas=[]
# nums=[]
# for i in range(5):
#     alphas.append(cards[i][0])
#     nums.append(cards[i][1])
# nums.sort()
# noNums=list(set(alphas))
# def check():
#     global cards
#     temp=0
#     if len(list(set(alphas)))==1:
#         # 1번 규칙
#         for i, num in enumerate(range(min(nums)+1, min(nums)+4), range(5)):
#             if nums[i]!=num:
#                 temp=1
#                 break
#         if temp==0:
#             return 900+max(nums)
#         # 4번 규칙
#         else:
#             return 600+max(nums)
#     elif len(noNums)==2:
#         first=nums.count(noNums[0])
#         second=nums.count(noNums[1])
#         ans=0
#         # 2번 규칙
#         if first==4:
#             ans=800+noNums[0]
#         elif second==4:
#             ans=800+noNums[1]
#         # 3번 규칙
#         elif first==3 and second==2:
#             ans=700+first*10+second
#         elif second==3 and first==2:
#             ans=700+second*10+first
#     elif len(noNums)==3:
#         ans=0
#         first=nums.count(noNums[0])
#         second=nums.count(noNums[1])
#         third=nums.count(noNums[2])
#         # 6번 규칙
#         if first==3:
#             ans=400+first
#         elif second==3:
#             ans=400+second
#         # 7번 규칙
#         elif first==2 and second==2:
#             ans=300+max(first,second)*10+min(first,second)
#         elif second==2 and third==2:
#             ans=300+max(second,third)*10+min(second,third)
#         elif first==2 and third==2:
#             ans=300+max(first,third)*10+min(first,third)
#         return ans
#     # 8번 규칙
#     elif len(noNums)==4:
#         first=nums.count(noNums[0])
#         second=nums.count(noNums[1])
#         third=nums.count(noNums[2])
#         fourth=nums.count(noNums[3])
#         return 200+max(first,second,third,fourth)
#         # 5번 규칙
#         for i, num in enumerate(range(min(nums)+1, min(nums)+4), range(5)):
#             if nums[i]!=num:
#                 temp=1
#                 break
#         if temp==0: return 500+max(nums)

#     # 9번 규칙
#     else: return 100+max(nums)
# print(check())