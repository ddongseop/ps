dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

L, N, Q = map(int, input().split())
field = [[2]*(L+2)]
for _ in range(L):
    field.append([2] + list(map(int, input().split())) + [2])
field.append([2]*(L+2))
users = {}
init_hp = {}

for index in range(11, 11+N): # 실제 기사 index 1이면 10 더해서 11로 매핑 필요
    r, c, h, w, k = map(int, input().split())
    new_user = {'row': r, 'col': c, 'h': h, 'w': w, 'hp': k}
    users[index] = new_user
    for i in range(r, r+h):
        for j in range(c, c+w):
            if field[i][j]:
                field[i][j] = 100 + index
            else:
                field[i][j] = index

    init_hp[index] = k

def check_range(row, col, h, w):
    report = []
    for r in range(row, row+h):
        for c in range(col, col+w):
            if field[r][c] == 1 or field[r][c] == 2:
                report.append(field[r][c])
            elif field[r][c] > 100:
                report.append(field[r][c] - 100)
                report.append(1)
            elif field[r][c] > 10:
                report.append(field[r][c])
    return report

def check_can_move(index, direction, ans):
    r = users[index]['row']
    c = users[index]['col']
    new_r = r + dr[direction]
    new_c = c + dc[direction]

    h = users[index]['h']
    w = users[index]['w']

    report = sorted(check_range(new_r, new_c, h, w))
    if 2 in report: # 만약 벽이 있으면
        return []
    elif report and report[-1] >= 11: # 만약 기사가 한명이라도 있으면
        for re in report:
           if re >= 11 and re != index and re not in ans:
               result = check_can_move(re, direction, ans+[re])
               if len(result) == 0:
                   return []
               else:
                   ans += result
    return ans

def move_user_dict(index, direction):
    r = users[index]['row']
    c = users[index]['col']
    h = users[index]['h']
    w = users[index]['w']

    for i in range(r, r+h):
        for j in range(c, c+w):
            if field[i][j] > 100:
                field[i][j] = 1
            else:
                field[i][j] = 0

    users[index]['row'] += dr[direction]
    users[index]['col'] += dc[direction]

def re_arrange_user():
    for index in list(users.keys()):
        if users[index]['hp'] > 0:
            r = users[index]['row']
            c = users[index]['col']
            h = users[index]['h']
            w = users[index]['w']

            for i in range(r, r + h):
                for j in range(c, c + w):
                    if field[i][j] == 1 or field[i][j] > 100:
                        field[i][j] = 100 + index
                    else:
                        field[i][j] = index

for sec in range(Q):
    i, direction = map(int, input().split())
    index = i+10

    if users[index]['hp'] <= 0:
        continue

    ans = list(set(check_can_move(index, direction, [index])))

    for a in ans:
        # 기사 이동시키기
        move_user_dict(a, direction)

        if a == index: # 자기 자신은 데미지 안입음
            continue
        else: # 밀려난 기사들은 데미지 입음
            report = check_range(users[a]['row'], users[a]['col'], users[a]['h'], users[a]['w'])
            damage = 0
            for r in report:
                if r == 1: damage += 1
            users[a]['hp'] -= damage

    # 기사 필드에 재배치
    re_arrange_user()

ans = 0
for index in list(users.keys()):
    if users[index]['hp'] > 0:
        ans += init_hp[index] - users[index]['hp']
print(ans)