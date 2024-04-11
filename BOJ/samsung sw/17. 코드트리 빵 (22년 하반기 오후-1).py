from collections import deque
# import sys
# sys.stdin = open("sample_input.txt", "r")
# T = int(input())

N, M = 0, 0
field = [[0]*N for _ in range(N)]
users = {}
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

def init():
    N, M = 0, 0
    field = [[0]*N for _ in range(N)]
    users = {}

def find_user_direction(index):
    cur_x, cur_y = users[index]['cur_x'], users[index]['cur_y']
    target_x, target_y = users[index]['target_x'], users[index]['target_y']

    visited = [[False] * N for _ in range(N)]
    visited[cur_y][cur_x] = True
    queue = deque([[0, cur_x, cur_y, []]])

    candidates = []
    minimum = 1000
    while queue:
        distance, cur_x, cur_y, route = queue.popleft()
        if cur_x == target_x and cur_y == target_y:
            if distance < minimum:
                minimum = distance
                candidates = [route]
            elif distance == minimum:
                candidates.append(route)

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if nx > N - 1 or nx < 0 or ny > N - 1 or ny < 0: continue
            if field[ny][nx] == 3 or visited[ny][nx] == True: continue
            queue.append([distance + 1, nx, ny, route + [i]])
            visited[ny][nx] = True

    direction = sorted(candidates)[0][0]
    return direction

def users_move(m):

    lock_list = []

    for index in range(1, m+1):
        if users[index]['finish'] or (users[index]['cur_x'] == -1 and users[index]['cur_y'] == -1):
            continue
        direction = find_user_direction(index)
        nx = users[index]['cur_x'] + dx[direction]
        ny = users[index]['cur_y'] + dy[direction]

        users[index]['cur_x'] = nx
        users[index]['cur_y'] = ny
        if users[index]['target_x'] == nx and users[index]['target_y'] == ny:
            users[index]['finish'] = True
            lock_list.append([nx, ny])

    return lock_list

def find_distance_target_to_basecamp(index, base_x, base_y):
    cur_x, cur_y = users[index]['target_x'], users[index]['target_y']

    visited = [[False] * N for _ in range(N)]
    visited[cur_y][cur_x] = True
    queue = deque([[0, cur_x, cur_y]])

    minimum = 1000
    while queue:
        distance, cur_x, cur_y = queue.popleft()
        if cur_x == base_x and cur_y == base_y:
            if distance < minimum:
                minimum = distance

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if nx > N - 1 or nx < 0 or ny > N - 1 or ny < 0: continue
            if field[ny][nx] == 3 or visited[ny][nx] == True: continue
            queue.append([distance + 1, nx, ny])
            visited[ny][nx] = True

    return minimum

def locate_to_basecamp(index):
    lock_list = []
    candidates = []
    for y in range(N):
        for x in range(N):
            if field[y][x] == 1:
                distance = find_distance_target_to_basecamp(index, x, y)
                candidates.append([distance, y, x])
    distance, y, x = sorted(candidates)[0]
    users[index]['cur_x'] = x
    users[index]['cur_y'] = y
    lock_list.append([x, y])

    return lock_list

for test_case in range(1):
    init()

    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]

    for index in range(1, M+1):
        new = {}
        new['cur_x'], new['cur_y'] = -1, -1
        target_y, target_x = map(int, input().split())
        new['target_x'], new['target_y'] = target_x-1, target_y-1
        new['finish'] = False
        users[index] = new

        field[target_y-1][target_x-1] = 2

    minute = 0
    while True:
        minute += 1
        if minute > M:
            m = M
        else: m = minute

        # 1. 유저들 편의점으로 이동
        lock_list = users_move(m)
        for x, y in lock_list:
            field[y][x] = 3

        # 2. 유저들 베이스 캠프로 할당
        if minute <= M:
            lock_list = locate_to_basecamp(m)
            for x, y in lock_list:
                field[y][x] = 3

        # 4. 유저들이 모두 도착했나 확인
        signal = True
        for index in range(1, M+1):
            if users[index]['finish'] == False:
                signal = False
                break
        if signal:
            print(minute)
            break

        # print(users)
        # print(field)