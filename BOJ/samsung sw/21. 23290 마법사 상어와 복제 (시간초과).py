import copy

field = [[[] for _ in range(4)] for _ in range(4)]
fishes = {}
M, S = 0, 0
fish_index, smell_index = 1, -1

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
sx = [0, -1, 0, 1]
sy = [-1, 0, 1, 0]

maximum = 0
candidates = []

def init():
    global field, fishes, M, S, fish_index, smell_index
    field = [[[] for _ in range(4)] for _ in range(4)]
    fishes = {}
    M, S = 0, 0
    fish_index, smell_index = 1, -1

    global maximum, candidates
    maximum = 0
    candidates = []


def append_fish(x, y, direction):
    global fish_index
    fishes[fish_index] = {'x': x, 'y': y, 'tmp': direction}
    field[y][x].append(fish_index)
    fish_index += 1

def copy_magic(past_field, past_fishes):
    for y in range(4):
        for x in range(4):
            cur_list = past_field[y][x]
            cur_list.sort(reverse=True)
            for index in cur_list:
                if index <= 0: break
                append_fish(past_fishes[index]['x'], past_fishes[index]['y'], past_fishes[index]['tmp'])

def fishes_move():
    cur_list = list(fishes.keys())
    cur_list.sort(reverse=True)
    for index in cur_list:
        if index <= 0: break

        x = fishes[index]['x']
        y = fishes[index]['y']
        direction = fishes[index]['tmp']

        can_move = False
        for _ in range(8):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or nx > 3 or ny < 0 or ny > 3:
                direction -= 1
                if direction < 0: direction = 7
                continue

            cur_list = field[ny][nx]
            if 0 in cur_list or (len(cur_list) > 0 and min(cur_list) < 0):
                direction -= 1
                if direction < 0: direction = 7
                continue

            can_move = True
            break

        if can_move:
            fishes[index]['x'] = x+dx[direction]
            fishes[index]['y'] = y+dy[direction]
            fishes[index]['tmp'] = direction

            field[y][x].remove(index)
            field[y+dy[direction]][x+dx[direction]].append(index)

def find_shark_route(cur_x, cur_y, cnt, route, kill):
    if cnt == 3:
        global candidates, maximum
        if kill > maximum:
            maximum = kill
            candidates = [route]
        elif kill == maximum:
            candidates.append(route)
        return

    x = cur_x
    y = cur_y
    for direction in range(4):
        nx = x + sx[direction]
        ny = y + sy[direction]
        if nx < 0 or nx > 3 or ny < 0 or ny > 3: continue

        cur_kill = 0
        cur_list = field[ny][nx]
        cur_list.sort(reverse=True)
        for index in cur_list:
            if index < 0: break
            cur_kill += 1

        if len(route) and nx == x - sx[route[-1]] and ny == y - sy[route[-1]]:
            cur_kill = 0

        find_shark_route(nx, ny, cnt+1, route+[direction], kill+cur_kill)

def shark_move(direction):
    x = fishes[0]['x']
    y = fishes[0]['y']
    nx = x + sx[direction]
    ny = y + sy[direction]

    fishes[0]['x'] = nx
    fishes[0]['y'] = ny
    field[y][x].remove(0)
    field[ny][nx].append(0)

    fish_eat = False
    cur_list = copy.deepcopy(field[ny][nx])
    cur_list.sort(reverse=True)
    for index in cur_list:
        if index <= 0: break
        fish_eat = True
        del fishes[index]
        field[ny][nx].remove(index)

    if fish_eat:
        global smell_index
        fishes[smell_index] = {'x': nx, 'y': ny, 'tmp': 3}
        field[ny][nx].append(smell_index)
        smell_index -= 1

def smells_disappear():
    cur_list = list(fishes.keys())
    cur_list.sort()
    for index in cur_list:
        if index >= 0: break
        fishes[index]['tmp'] -= 1

        if fishes[index]['tmp'] == 0:
            field[fishes[index]['y']][fishes[index]['x']].remove(index)
            del fishes[index]

for test_case in range(1):
    init()
    M, S = map(int, input().split())
    for _ in range(M):
        y, x, direction = map(int, input().split())
        append_fish(x-1, y-1, direction-1)
    y, x = map(int, input().split())
    fishes[0] = {'x': x-1, 'y': y-1, 'tmp': -1}
    field[y-1][x-1].append(0)

    for _ in range(S):

        # 1. 미리 복제해두기
        past_field = copy.deepcopy(field)
        past_fishes = copy.deepcopy(fishes)

        # 2. 물고기 이동
        fishes_move()

        # 3. 상어 이동
        maximum = 0
        candidates = []
        find_shark_route(fishes[0]['x'], fishes[0]['y'], 0, [], 0)
        route = sorted(candidates)[0]

        for direction in route:
            shark_move(direction)

        # 4. 냄새 사라지게 만들기
        smells_disappear()

        # 5. 미리 복제해둔 field로 마법 발동
        copy_magic(past_field, past_fishes)

    ans = 0
    cur_list = list(fishes.keys())
    cur_list.sort(reverse=True)
    for index in cur_list:
        if index <= 0: break
        ans += 1
    print(ans)
