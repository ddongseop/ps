import copy

original_field = [[0] * 4 for _ in range(4)]
original_fishes = {}
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
maximum = 0

for x in range(4):
    cur_row = list(map(int, input().split()))
    for y in range(4):
        index = cur_row[2 * y]

        original_field[x][y] = index
        original_fishes[index] = {'x': x, 'y': y, 'direction': cur_row[2 * y + 1]-1}
original_fishes = dict(sorted(original_fishes.items()))

def shark_eat(target_x, target_y, field, fishes):
    target_index = field[target_x][target_y]

    if 20 in list(fishes.keys()):
        field[fishes[20]['x']][fishes[20]['y']] = 0
    field[target_x][target_y] = 20

    fishes[20] = {'direction': fishes[target_index]['direction'],  # 상어의 index를 20으로 지정
                  'x': fishes[target_index]['x'],
                  'y': fishes[target_index]['y']}
    del fishes[target_index]


def move_fish(index, field, fishes):
    direction = fishes[index]['direction']
    x = fishes[index]['x']
    y = fishes[index]['y']

    # 1. 물고기가 움직일 방향을 탐색
    for _ in range(8):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if (0 <= nx <= 3 and 0 <= ny <= 3) and field[nx][ny] != 20:  # 상어면 안됨
            # 2. 실제로 이동을 수행
            target = field[nx][ny]

            fishes[index]['x'] = nx
            fishes[index]['y'] = ny
            if target == 0:  # 물고기가 빈칸으로 가는거라면
                field[x][y], field[nx][ny] = 0, index
            else:  # 물고기가 빈칸으로 가는게 아니라면
                fishes[target]['x'] = x
                fishes[target]['y'] = y
                field[x][y], field[nx][ny] = target, index
            fishes[index]['direction'] = direction
            break

        direction += 1
        if direction > 7: direction = 0  # 45도씩 왼쪽으로 회전


def count_shark_movement(field, fishes):
    x = fishes[20]['x']
    y = fishes[20]['y']
    direction = fishes[20]['direction']

    count = 1
    counts = []
    while True:
        nx = x + count * dx[direction]
        ny = y + count * dy[direction]

        if nx < 0 or nx > 3 or ny < 0 or ny > 3:
            break
        if field[nx][ny] != 0:
            counts.append(count)

        count += 1

    return counts

def simulate(depth, cur_point, tmp_field, tmp_fishes):

    for index in list(tmp_fishes.keys()):
        if index != 20:
            move_fish(index, tmp_field, tmp_fishes)

    counts = count_shark_movement(tmp_field, tmp_fishes)
    if len(counts) == 0:
        global maximum
        if cur_point > maximum:
            maximum = cur_point

    for count in counts:
        nx = tmp_fishes[20]['x'] + (count * dx[tmp_fishes[20]['direction']])
        ny = tmp_fishes[20]['y'] + (count * dy[tmp_fishes[20]['direction']])
        point = tmp_field[nx][ny]

        new_field = copy.deepcopy(tmp_field)
        new_fishes = copy.deepcopy(tmp_fishes)
        shark_eat(nx, ny, new_field, new_fishes)
        simulate(depth+1, cur_point + point, new_field, new_fishes)


start = original_field[0][0]
shark_eat(0, 0, original_field, original_fishes)
simulate(1, start, original_field, original_fishes)
print(maximum)
