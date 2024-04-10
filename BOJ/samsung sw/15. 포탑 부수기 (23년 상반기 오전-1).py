from collections import deque

N, M, K = map(int, input().split())
field = [[-1]*(M+2)]
recent_attack = [[-1]*(M+2)]

for _ in range(N):
    field.append(([-1] + list(map(int, input().split())) + [-1]))
    recent_attack.append([-1] + [0]*M + [-1])
field.append([-1]*(M+2))
recent_attack.append([-1]*(M+2))

def find_attacker_and_target():
    candidates = []
    for j in range(1, N+1):
        for i in range(1, M+1):
            if field[j][i] > 0:
               candidates.append([-1*field[j][i], recent_attack[j][i], i+j, i])
    candidates.sort(reverse=True)
    return candidates

dx = [1, 0, -1, 0, 1, 1, -1, -1, 0]
dy = [0, 1, 0, -1, -1, 1, 1, -1, 0]

def calculate(nx, ny):
    if nx < 1: nx = M
    if nx > M: nx = 1
    if ny < 1: ny = N
    if ny > N: ny = 1

    return [nx, ny]

def check_lazer_available(Ax, Ay, Tx, Ty):
    shortest_distance = 1000

    visited = [[False]*(M+2) for _ in range(N+2)]
    visited[Ay][Ax] = True

    queue = deque([[0, Ax, Ay, []]])
    ans = []
    while queue:

        tmp = queue.popleft()
        cur_distance, cur_x, cur_y, route = tmp[0], tmp[1], tmp[2], tmp[3]
        if cur_distance > shortest_distance: continue
        elif cur_distance < shortest_distance and cur_x == Tx and cur_y == Ty:
            shortest_distance = cur_distance
            ans = [route]
        elif cur_distance == shortest_distance and cur_x == Tx and cur_y == Ty:
            ans.append(route)

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            nx, ny = calculate(nx, ny)

            if visited[ny][nx] == True or field[ny][nx] <= 0: continue
            visited[ny][nx] = True

            queue.append([cur_distance+1, nx, ny, route+[i]])

    return ans

def lazer_attack(route, done, Ax, Ay, Tx, Ty):
    cur_x, cur_y = Ax, Ay
    done[cur_y][cur_x] = True
    for direction in route:
        cur_x, cur_y = cur_x + dx[direction], cur_y + dy[direction]
        cur_x, cur_y = calculate(cur_x, cur_y)

        done[cur_y][cur_x] = True
        if cur_x == Tx and cur_y == Ty:
            field[cur_y][cur_x] -= field[Ay][Ax]
        else:
            field[cur_y][cur_x] -= (field[Ay][Ax] // 2)
        if field[cur_y][cur_x] < 0: field[cur_y][cur_x] = 0
    return done

def bomb_attack(done, Ax, Ay, Tx, Ty):
    done[Ay][Ax] = True
    for direction in range(9):
        cur_x, cur_y = Tx + dx[direction], Ty + dy[direction]
        cur_x, cur_y = calculate(cur_x, cur_y)

        done[cur_y][cur_x] = True
        if cur_x == Tx and cur_y == Ty:
            field[cur_y][cur_x] -= field[Ay][Ax]
        elif cur_x == Ax and cur_y == Ay:
            continue
        else:
            field[cur_y][cur_x] -= (field[Ay][Ax] // 2)
        if field[cur_y][cur_x] < 0: field[cur_y][cur_x] = 0
    return done

for i in range(1, K+1):
    # 1. attacker 선정, 2. target 설정
    candidates = find_attacker_and_target()
    Ax, Ay = candidates[0][3], (candidates[0][2]-candidates[0][3])
    field[Ay][Ax] += (N+M)
    recent_attack[Ay][Ax] = i
    Tx, Ty = candidates[-1][3], (candidates[-1][2]-candidates[-1][3])

    # 3. 레이저 공격 가능 여부 체크
    ans = check_lazer_available(Ax, Ay, Tx, Ty)

    # 4-1. 레이저 공격
    if len(ans) > 0:
        route = sorted(ans)[0]
        done = lazer_attack(route, [[False]*(M+2) for _ in range(N+2)], Ax, Ay, Tx, Ty)
    # 4-2. 포탄 공격
    else:
        done = bomb_attack([[False]*(M+2) for _ in range(N+2)], Ax, Ay, Tx, Ty)

    survive = 0
    for j in range(1, N+1):
        for i in range(1, M+1):
            if field[j][i] > 0: survive += 1
    if survive <= 1: break

    # 5. 포탑 정비
    for j in range(1, N + 1):
        for i in range(1, M + 1):
            if done[j][i] == False and field[j][i] > 0:
                field[j][i] += 1

maximum = -1
for j in range(1, N+1):
    for i in range(1, M+1):
        if field[j][i] > maximum:
            maximum = field[j][i]
print(maximum)