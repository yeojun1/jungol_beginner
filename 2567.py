N, P = map(int, input().split())
cycle = []
tmp = N

while tmp not in cycle:
    cycle.append(tmp)
    tmp = tmp * N % P

# 순환 시작점부터 순환 길이 계산
cycle_start_index = cycle.index(tmp)
cycle_length = len(cycle) - cycle_start_index

print(cycle_length)