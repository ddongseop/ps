import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
field = [[0]*C for _ in range(R)]
sharks = {}

for index in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    
    field[r-1][c-1] = index

    new_shark = {}
    new_shark['row'] = r-1
    new_shark['col'] = c-1
    new_shark['speed'] = s
    new_shark['direction'] = d
    new_shark['size'] = z
    sharks[index] = new_shark

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]
def shark_simulate():
    for key in sharks.keys():
        row = sharks[key]['row']
        col = sharks[key]['col']
        direction = sharks[key]['direction']
        field[row][col] = 0

        speed = sharks[key]['speed']

        for _ in range(speed):
            row += dr[direction]
            col += dc[direction]
            
            if row > R-1:
                direction = 1
            elif row < 0:
                direction = 2
            elif col > C-1:
                direction = 4
            elif col < 0:
                direction = 3
            else:
                continue
        
            row += 2*dr[direction]
            col += 2*dc[direction]

        sharks[key]['row'] = row
        sharks[key]['col'] = col
        sharks[key]['direction'] = direction
    
    del_list = []
    for key in sharks.keys():
        row = sharks[key]['row']
        col = sharks[key]['col']

        if field[row][col]:
            if sharks[key]['size'] > sharks[field[row][col]]['size']:
                del_list.append(field[row][col])
                field[row][col] = key
            else:
                del_list.append(key)
        else:
            field[row][col] = key
    for key in del_list:
        del sharks[key]    

answer = 0
for c in range(C):
    for r in range(R):
        if field[r][c]:
            answer += sharks[field[r][c]]['size']
            del sharks[field[r][c]]
            field[r][c] = 0
            break
    shark_simulate()

print(answer)