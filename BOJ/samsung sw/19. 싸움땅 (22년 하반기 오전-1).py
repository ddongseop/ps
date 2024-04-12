N, M, K = 0, 0, 0
field = []
users = {}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def init():
    N, M, K = 0, 0, 0
    field = []
    users = {}


def is_user_exist(x, y, my_index):
    for index in list(users.keys()):
        cur_x = users[index]['x']
        cur_y = users[index]['y']
        if cur_x == x and cur_y == y and index != my_index:
            return index
    return 0

def user_move(index):

    cur_x = users[index]['x']
    cur_y = users[index]['y']
    direction = users[index]['direction']

    nx = cur_x + dx[direction]
    ny = cur_y + dy[direction]

    if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
        if direction == 0: direction = 2
        elif direction == 1: direction = 3
        elif direction == 2: direction = 0
        elif direction == 3: direction = 1
        users[index]['direction'] = direction

        nx = cur_x + dx[direction]
        ny = cur_y + dy[direction]

    users[index]['x'] = nx
    users[index]['y'] = ny


def find_winner_and_get_point(me, opponent):
    my_ablility = users[me]['stat'] + users[me]['weapon']
    opponent_ability = users[opponent]['stat'] + users[opponent]['weapon']

    if my_ablility > opponent_ability:
        users[me]['point'] += my_ablility - opponent_ability
        return me, opponent
    elif opponent_ability > my_ablility:
        users[opponent]['point'] += opponent_ability - my_ablility
        return opponent, me
    elif users[me]['stat'] > users[opponent]['stat']:
        return me, opponent
    else:
        return opponent, me

def swap_weapon(index):
    cur_x = users[index]['x']
    cur_y = users[index]['y']
    cur_weapon = users[index]['weapon']

    if len(field[cur_x][cur_y]) == 0:
        return

    weapon_list = sorted(field[cur_x][cur_y])
    top_weapon = weapon_list[-1]

    if top_weapon > cur_weapon:
        users[index]['weapon'] = weapon_list.pop()
        if cur_weapon > 0:
            weapon_list.append(cur_weapon)
        field[cur_x][cur_y] = weapon_list

def loser_task(index):
    cur_x = users[index]['x']
    cur_y = users[index]['y']
    cur_weapon = users[index]['weapon']

    # 1. 총을 격자에 내려놓기
    users[index]['weapon'] = 0
    if cur_weapon > 0:
        field[cur_x][cur_y].append(cur_weapon)

    # 2. 방향을 탐색
    direction = users[index]['direction']

    for i in range(4):
        nx = cur_x + dx[direction]
        ny = cur_y + dy[direction]

        if 0 <= nx <= N-1 and 0 <= ny <= N-1 and is_user_exist(nx, ny, index) == 0:
            break

        if i == 3: print("플레이어가 갈 수 있는 방향이 없습니다.")
        direction += 1
        if direction > 3: direction = 0

    users[index]['direction'] = direction

    # 3. 방향으로 1칸 이동
    users[index]['x'] = cur_x + dx[direction]
    users[index]['y'] = cur_y + dy[direction]


for test_case in range(1):
    init()
    N, M, K = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if field[x][y] != 0:
                field[x][y] = [field[x][y]]
            else:
                field[x][y] = []

    for index in range(1, M+1):
        x, y, d, s = map(int, input().split())
        users[index] = {'x': x - 1, 'y': y - 1, 'direction': d, 'stat': s, 'weapon': 0, 'point': 0}

    for turn in range(1, K+1):
        # 유저별로 턴 수행
        for index in list(users.keys()):
            # 1. 일단 유저 이동
            user_move(index)

            cur_x = users[index]['x']
            cur_y = users[index]['y']
            opponent = is_user_exist(cur_x, cur_y, index)

            # 2-1. 이동한 칸에 사람이 있으면
            if opponent:
                winner, loser = find_winner_and_get_point(index, opponent)
                loser_task(loser)
                swap_weapon(loser)
                swap_weapon(winner)
            # 2-2. 이동한 칸에 총이 있거나 빈칸이면
            else:
                swap_weapon(index)

    ans = []
    for index in list(users.keys()):
        ans.append(users[index]['point'])
    print(*ans)