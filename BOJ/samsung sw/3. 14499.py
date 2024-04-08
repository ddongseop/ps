import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

dice = [None, 0, 0, 0, 0, 0, 0]
dx = [None, 0, 0, -1, 1]
dy = [None, 1, -1, 0, 0]

top = 1
forward = 5
right = 3
for command in commands:
    if (command == 1 and y == M-1) or (command == 2 and y == 0) or (command == 3 and x == 0) or (command == 4 and x == N-1):
        continue

    if command == 1:
        bottom = right
        right = top
    elif command == 2:
        bottom = 7 - right
        right = 7 - top
    elif command == 3:
        bottom = 7 - forward
        forward = 7 - top
    elif command == 4:
        bottom = forward
        forward = top

    top = 7 - bottom
    x += dx[command]
    y += dy[command]

    if board[x][y] == 0:
        board[x][y] = dice[bottom]
    else:
        dice[bottom] = board[x][y]
        board[x][y] = 0

    print(dice[top])