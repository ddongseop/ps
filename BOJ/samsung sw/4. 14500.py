import sys
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

maximum = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False]*M for _ in range(N)]

def dfs(x, y, sum, cnt):
    global maximum
    if cnt == 4:
        maximum = max(sum, maximum)
        return
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if nx < 0 or nx > M-1 or ny < 0 or ny > N-1 or visited[ny][nx]:
            continue
        visited[ny][nx] = True
        dfs(nx, ny, sum+paper[ny][nx], cnt+1)
        visited[ny][nx] = False

def specialfs(x, y):
    global maximum
    cnt = paper[y][x]

    direction = []
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
            continue
        direction.append(paper[ny][nx])
    if len(direction) == 4:
        direction.sort(reverse=True)
        direction.pop()
        maximum = max(maximum, cnt + sum(direction))
    elif len(direction) == 3:
        maximum = max(maximum, cnt + sum(direction))
    return

for i in range(N):
    for j in range(M):       
        visited[i][j] = True
        dfs(j, i, paper[i][j], 1)
        specialfs(j, i)
        visited[i][j] = False

print(maximum)