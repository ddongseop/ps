import sys
input = sys.stdin.readline
from collections import deque

M, N, K = map(int, input().split())
field = [[False]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            field[y][x] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    field[y][x] = True
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and field[ny][nx] == False:
                field[ny][nx] = True
                queue.append((nx, ny))
                size += 1
    answer.append(size)

answer = []
for y in range(M):
    for x in range(N):
        if field[y][x] == False:
            bfs(x, y)

answer.sort()
print(len(answer))
print(*answer)