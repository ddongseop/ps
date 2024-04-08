import sys
input = sys.stdin.readline
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

room = []
cnt = 0
for x in range(N):
    curRow = list(map(int, input().split()))
    cnt += sum(curRow)
    room.append(curRow)

def cycle():
    queue = deque([(0, 0)])
    visited = [[0]*M for _ in range(N)]
    melt = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == -1:
                continue
            if room[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = -1
            elif room[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
            elif room[nx][ny] == 1 and visited[nx][ny] == 1:
                melt.append((nx, ny))
                visited[nx][ny] = -1

    global cnt
    for x, y in melt:
        room[x][y] = 0
        cnt -= 1
    
ans = 0
while cnt > 0:
    ans += 1
    cycle()
print(ans)