import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(M)]

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]
cnt = 0

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    field[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if (0 <= ny < M) and (0 <= nx < N) and field[ny][nx] == 1:
                queue.append((ny, nx))
                field[ny][nx] = 0

for i in range(M):
    for j in range(N):
        if field[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)