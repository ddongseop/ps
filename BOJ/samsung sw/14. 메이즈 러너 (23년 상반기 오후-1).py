N, M, K = map(int, input().split())

field = [[-1]*(N+2)]
for _ in range(N):
    field.append([-1] + list(map(int, input().split())) + [-1])
field.append([-1]*(N+2))

users = {}
for index in range(1, M+1):
    y, x = map(int, input().split())
    new_user = {}
    new_user['y'] = y
    new_user['x'] = x
    new_user['move'] = 0
    new_user['exited'] = False
    users[index] = new_user

exit_y, exit_x = map(int, input().split()) # 회전할 때 업데이트 해줘야함
field[exit_y][exit_x] = 10

def calculate_distance(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

dx = [0, 0, -1, 1, 0] # 상/하/좌/우/이동X
dy = [-1, 1, 0, 0, 0]

def find_direction(x, y):
    minimum = 20
    candidates = []
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if field[ny][nx] == -1 or (field[ny][nx] > 0 and field[ny][nx] < 10):
            continue

        distance = calculate_distance(nx, ny, exit_x, exit_y)
        if distance < minimum:
            minimum = distance
            candidates = [i]
        elif distance == minimum:
            candidates.append(i)

    return sorted(candidates)[0]
def user_move(index):
    x = users[index]['x']
    y = users[index]['y']
    direction = find_direction(x, y)

    nx = users[index]['x'] + dx[direction]
    ny = users[index]['y'] + dy[direction]
    users[index]['x'] = nx
    users[index]['y'] = ny
    users[index]['move'] += (abs(dx[direction]) + abs(dy[direction]))

    if nx == exit_x and ny == exit_y:
        users[index]['exited'] = True

def find_square():
    ans_x = 0
    ans_y = 0
    size = 1
    user_exist = []
    while size < N and ans_x == 0 and ans_y == 0:
        size += 1
        for start_y in range(1, N+2-size):
            if ans_x != 0 and ans_y != 0: break

            for start_x in range(1, N+2-size):
                if ans_x != 0 and ans_y != 0: break

                end_y = start_y + size - 1
                end_x = start_x + size - 1

                if exit_x < start_x or exit_x > end_x or exit_y < start_y or exit_y > end_y:
                    continue

                for index in list(users.keys()):
                    if users[index]['exited'] == True:
                        continue

                    user_x = users[index]['x']
                    user_y = users[index]['y']
                    if user_x >= start_x and user_x <= end_x and user_y >= start_y and user_y <= end_y:
                        user_exist.append(index)
                        ans_x = start_x
                        ans_y = start_y

    return [ans_x, ans_y, size, user_exist]

def rolling(start_x, start_y, size, user_exist):
    new_field = [[0]*size for _ in range(size)]

    for j in range(size):
        for i in range(size):
            new_field[i][size - 1 - j] = field[j+start_y][i+start_x]
            for index in user_exist:
                user_x = users[index]['x']
                user_y = users[index]['y']
                if user_x == i+start_x and user_y == j+start_y:
                    if type(new_field[i][size - 1 - j]) != list:
                        new_field[i][size - 1 - j] = [index]
                    else:
                        new_field[i][size - 1 - j].append(index)

    global exit_x, exit_y
    for j in range(size):
        for i in range(size):
            if type(new_field[j][i]) == list:
                for index in new_field[j][i]:
                    users[index]['x'] = start_x + i
                    users[index]['y'] = start_y + j
                field[start_y + j][start_x + i] = 0
            else:
                if new_field[j][i] == 10:
                    exit_x = start_x+i
                    exit_y = start_y+j
                    field[start_y + j][start_x + i] = new_field[j][i]
                elif new_field[j][i] > 0:
                    field[start_y + j][start_x + i] = new_field[j][i] - 1
                elif new_field[j][i] == 0:
                    field[start_y + j][start_x + i] = new_field[j][i]

for _ in range(K):
    # 1. 참가자 이동
    for index in list(users.keys()):
        if users[index]['exited'] == True:
            continue
        user_move(index)
    cnt = 0
    for index in list(users.keys()):
        if users[index]['exited'] == True: cnt += 1
    if cnt >= M: break

    # 2. 미로 회전을 위한 사각형 탐색
    start_x, start_y, size, user_exist = find_square()

    # 3. 미로 회전
    rolling(start_x, start_y, size, user_exist)

ans = 0
for index in list(users.keys()):
    ans += users[index]['move']

print(ans)
print(exit_y, exit_x)