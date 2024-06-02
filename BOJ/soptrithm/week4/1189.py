import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
field = [list(input().rstrip()) for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0
def dfs(cur_x, cur_y, distance):
    if distance == K and cur_x == C-1 and cur_y == 0:
        global answer
        answer += 1
        return
    
    field[cur_y][cur_x] = 'T'
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if (0 <= nx < C and 0 <= ny < R and field[ny][nx] != 'T'):
            field[ny][nx] = 'T'
            dfs(nx, ny, distance+1)
            field[ny][nx]='.'

dfs(0, R-1, 1)
print(answer)