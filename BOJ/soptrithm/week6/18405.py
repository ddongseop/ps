from collections import deque
import sys

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

queue = []
for x in range(N):
    for y in range(N):
        if field[x][y] != 0:
            queue.append((field[x][y], x, y, 0))
queue = deque(sorted(queue))

while queue:
    num, x, y, time = queue.popleft()
    if time == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == 0:
            field[nx][ny] = num
            queue.append((num, nx, ny, time+1))

print(field[X-1][Y-1])