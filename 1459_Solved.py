# 2668
n = int(input())
graph = [[] for _ in range(n+1)]

for a in range(n):
    b = int(input())
    graph[b].append(a+1) # index는 0부터이므로

visited = [False] * (n+1) # 노드 방문 여부 확인

result = [] # 결과 집합
# route 는 집합
def dfs(node, route):
    route.add(node)
    visited[node] = True
    for i in graph[node]:
        if i not in route: # 방문하지 않았다면
            dfs(i, route.copy()) # copy 는 얉은 복사 -> 참조만 복사한 복사이다 즉 원래 route와 동일한 주소를 가리킴 
        else:# 이미 node가 route에 포함되어있으므로 사이클이 생기는 경우 
            result.extend(list(route)) # append 대신 extend를 써야 동일 배열에 이어서 추가가 된다. 
            return

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, set([]))
result.sort()
# 정수들의 개수 출력하기
print(len(result))
# 뽑힌 정수들을 오름차순으로 출력하기
for i in result:
    print(i)
