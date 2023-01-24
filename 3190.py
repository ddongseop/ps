import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 2

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dirDict = dict()
queue = deque()
queue.append((0, 0))

L = int(input())
for _ in range(L):
    X, C = input().split()
    dirDict[int(X)] = C

curX, curY = 0, 0
board[curY][curX] = 1
curDir = 0
ans = 0

def turn(command):
    global curDir
    if command == 'L':
        curDir = (curDir - 1) % 4
    else:
        curDir = (curDir + 1) % 4

while True:
    ans += 1
    curX += dx[curDir]
    curY += dy[curDir]

    if curX < 0 or curX >= N or curY < 0 or curY >= N:
        break

    if board[curY][curX] == 2:
        board[curY][curX] = 1
        queue.append((curY, curX))
        if ans in dirDict:
            turn(dirDict[ans])
    
    elif board[curY][curX] == 0:
        board[curY][curX] = 1
        queue.append((curY, curX))
        tailY, tailX = queue.popleft()
        board[tailY][tailX] = 0
        if ans in dirDict:
            turn(dirDict[ans])

    else:
        break

print(ans)