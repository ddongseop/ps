import sys
input = sys.stdin.readline

## 각 지점이 연관되어 있을 경우 한번에 갱신했어야 하는데 그때그때 갱신해서 틀림

N, M = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

dp = [10000] * M
stack = []
for i in range(M):
    stack.append((i, 0, 0, field[0][i]))

while stack:
    cur_x, cur_y, direction, cost = stack.pop()
    if cur_y == N-1:
        dp[cur_x] = min(dp[cur_x], cost)

    if direction != 1:
        next_x, next_y = cur_x-1, cur_y+1
        if next_x < 0 or next_x > M-1 or next_y < 0 or next_y > N-1:
            pass
        else:
            stack.append((next_x, next_y, 1, cost+field[next_y][next_x]))
    if direction != 2:
        next_x, next_y = cur_x, cur_y+1
        if next_x < 0 or next_x > M-1 or next_y < 0 or next_y > N-1:
            pass
        else:
            stack.append((next_x, next_y, 2, cost+field[next_y][next_x]))
    if direction != 3:
        next_x, next_y = cur_x+1, cur_y+1
        if next_x < 0 or next_x > M-1 or next_y < 0 or next_y > N-1:
            pass
        else:
            stack.append((next_x, next_y, 3, cost+field[next_y][next_x]))

print(min(dp))