import sys

input = sys.stdin.readline

N, M, P, C, D = map(int, input().split())
field = [[0] * N for _ in range(N)]

R_r, R_c = map(int, input().split())
R_r -= 1
R_c -= 1
field[R_r][R_c] = 100  # 루돌프의 번호를 100으로 설정

santas = {}
for _ in range(P):
    index, S_r, S_c = map(int, input().split())

    new_santa = {}
    new_santa['row'] = S_r - 1
    new_santa['col'] = S_c - 1
    new_santa['out'] = False
    new_santa['stunned'] = 0
    new_santa['score'] = 0

    santas[index] = new_santa
    field[S_r - 1][S_c - 1] = index


def calculate_dist(R_r, R_c, S_r, S_c):
    return (R_r - S_r) ** 2 + (R_c - S_c) ** 2


def find_closest_santa():
    minimum_candidates = []
    minimum_dist = 10000
    for index in santas.keys():
        if santas[index]['out']:
            continue

        S_r = santas[index]['row']
        S_c = santas[index]['col']

        cur_dist = calculate_dist(R_r, R_c, S_r, S_c)
        if cur_dist == minimum_dist:
            minimum_candidates.append([S_r, S_c, index])
            minimum_dist = cur_dist
        elif cur_dist < minimum_dist:
            minimum_candidates = [[S_r, S_c, index]]
            minimum_dist = cur_dist

    minimum_candidates.sort(reverse=True)
    return minimum_candidates[0]


dr = [-1, 0, 1, 0, -1, 1, 1, -1, 0]
dc = [0, 1, 0, -1, 1, 1, -1, -1, 0]


def find_rudol_direction(target_santa):
    S_r = target_santa[0]
    S_c = target_santa[1]

    direction = 9
    minimum_dist = 10000
    for i in range(8):
        cur_dist = calculate_dist(R_r + dr[i], R_c + dc[i], S_r, S_c)
        if cur_dist <= minimum_dist:
            direction = i
            minimum_dist = cur_dist

    return direction


def move_santa(direction, index, point):
    S_r = santas[index]['row']
    S_c = santas[index]['col']
    new_S_r = S_r + point * dr[direction]
    new_S_c = S_c + point * dc[direction]

    if new_S_r > N - 1 or new_S_r < 0 or new_S_c > N - 1 or new_S_c < 0:  # 게임판 밖으로 산타가 날라갔을 경우
        field[S_r][S_c] = 0
        santas[index]['row'] = -1
        santas[index]['col'] = -1
        santas[index]['out'] = True

    elif field[new_S_r][new_S_c] and field[new_S_r][new_S_c] != index:  # 다른 산타가 있을 경우

        target_index = field[new_S_r][new_S_c]  # 재귀적으로 1씩 산타 옮기기
        move_santa(direction, target_index, 1)

        # 현재 산타 옮기기
        field[S_r][S_c] = 0
        field[new_S_r][new_S_c] = index
        santas[index]['row'] = new_S_r
        santas[index]['col'] = new_S_c

    else:  # 그냥 무사히 날라갔을 경우
        field[S_r][S_c] = 0
        field[new_S_r][new_S_c] = index
        santas[index]['row'] = new_S_r
        santas[index]['col'] = new_S_c


def collidle(direction, index, point, signal):
    santas[index]['stunned'] = 2
    santas[index]['score'] += point

    if signal:
        move_santa(direction, index, point - 1)
    else:
        move_santa(direction, index, point)


def find_santa_direction(santa_index):
    S_r = santas[santa_index]['row']
    S_c = santas[santa_index]['col']

    direction = 8
    minimum_dist = calculate_dist(R_r, R_c, S_r, S_c)
    for i in range(3, -1, -1):
        new_S_r = S_r + dr[i]
        new_S_c = S_c + dc[i]
        cur_dist = calculate_dist(R_r, R_c, new_S_r, new_S_c)
        if new_S_r > N - 1 or new_S_r < 0 or new_S_c > N - 1 or new_S_c < 0:
            continue
        elif field[new_S_r][new_S_c] > 0 and field[new_S_r][new_S_c] <= 30:
            continue
        if cur_dist <= minimum_dist:
            direction = i
            minimum_dist = cur_dist

    return direction


for m in range(M):

    # 1. 루돌프 이동
    target_santa = find_closest_santa()
    direction = find_rudol_direction(target_santa)

    new_R_r = R_r + dr[direction]
    new_R_c = R_c + dc[direction]

    if field[new_R_r][new_R_c]:  # 산타와 충돌이 일어날 경우
        index = field[new_R_r][new_R_c]
        collidle(direction, index, C, 0)

    field[R_r][R_c] = 0
    field[new_R_r][new_R_c] = 100
    R_r = new_R_r
    R_c = new_R_c

    # 2. 산타 이동
    index_list = sorted(list(santas.keys()))
    for index in index_list:
        cur_santa = santas[index]
        S_r = cur_santa['row']
        S_c = cur_santa['col']

        if cur_santa['stunned'] > 0 or cur_santa['out'] == True:
            continue

        direction = find_santa_direction(index)

        new_S_r = S_r + dr[direction]
        new_S_c = S_c + dc[direction]

        if field[new_S_r][new_S_c] == 100:  # 루돌프와 충돌이 일어날 경우
            if direction == 0:
                direction = 2
            elif direction == 1:
                direction = 3
            elif direction == 2:
                direction = 0
            elif direction == 3:
                direction = 1
            collidle(direction, index, D, 1)

        else:
            field[S_r][S_c] = 0
            field[new_S_r][new_S_c] = index
            cur_santa['row'] = new_S_r
            cur_santa['col'] = new_S_c

    # 3. 매 루프 검증할 것
    cnt = 0
    for key in santas.keys():
        cur_santa = santas[key]
        if cur_santa['stunned'] > 0:
            cur_santa['stunned'] -= 1
        if cur_santa['out'] == False:
            cnt += 1
            cur_santa['score'] += 1

    if cnt == 0:
        break

ans = []
index_list = sorted(list(santas.keys()))
for index in index_list:
    ans.append(santas[index]['score'])
print(*ans)