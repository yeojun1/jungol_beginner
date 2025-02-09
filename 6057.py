from collections import deque

def pizza_sales(P,N,actions):
    pizza_queues=[deque() for _ in range(P+1)]

    total_sales=0

    for action in actions:
        cmd,p=action[0],action[1]

        if cmd==0:
            m=action[2]
            pizza_queues[p].append(m)

        elif cmd==1:
            if pizza_queues[p]:
                total_sales+=pizza_queues[p].popleft()
                
    return total_sales

P,N=map(int,input().split())
actions=[]

for _ in range(N):
    cmd_input=list(map(int,input().split()))
    actions.append(cmd_input)

result=pizza_sales(P,N,actions)
print(result)

# _,N=map(int,input().split())
# queue=[]
# a=0
# for _ in range(N):
#     inp=list(map(int,input().split()))
#     if inp[0]==1:
#         for i in range(len(queue)):
#             if queue[i][0]==inp[1]:
#                 a+=queue[i][1]
#                 queue.pop(i)
#                 break
#     else:
#         queue.append([inp[1],inp[2]])
# print(a)