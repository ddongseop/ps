N, M, R = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def rotate():
    cur_width = M
    cur_height = N
    start_x = 0
    start_y = 0
    cnt = 0
    while cur_width >= 2 and cur_height >= 2:
        cur_x = start_x
        cur_y = start_y
        tmp1 = field[cur_y][cur_x]
        tmp2 = 0
        for i in range(4):
            while True:
                next_x = cur_x+dx[i]
                next_y = cur_y+dy[i]
                if next_x < 0+cnt or next_x > M-1-cnt or next_y < 0+cnt or next_y > N-1-cnt:
                    tmp1 = tmp2
                    break
                tmp2 = field[next_y][next_x]
                field[next_y][next_x] = tmp1
                tmp1 = tmp2

                cur_x = next_x
                cur_y = next_y

        cur_width -= 2
        cur_height -= 2
        start_x += 1
        start_y += 1
        cnt += 1


for _ in range(R):
    rotate()
for row in field:
    print(*row)