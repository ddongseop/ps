from collections import deque
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

visited = [[False]*5 for _ in range(5)]
visited[r][c] = True
queue = deque([(r, c, 0)])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
minimum = 1000
while queue:
    r, c, cur = queue.popleft()
    if board[r][c] == 1:
        if cur < minimum:
            minimum = cur
        continue

    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        if ny < 0 or ny > 4 or nx < 0 or nx > 4: continue
        if board[ny][nx] == -1 or visited[ny][nx]: continue
        visited[ny][nx] = True
        queue.append((ny, nx, cur+1))

if minimum == 1000:
    print(-1)
else:
    print(minimum)