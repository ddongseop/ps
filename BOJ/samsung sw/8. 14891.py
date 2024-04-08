import sys
input = sys.stdin.readline

topni = [list(map(int, input().strip())) for _ in range(4)]
point = [0]*4
K = int(input())
for _ in range(K):
    target, direction = map(int, input().split())
    change = [[target-1, direction]]
    
    cur_direction = direction
    for i in range(target-2, -1, -1): # 왼쪽 방향으로 탐색
        my_index = i+1
        neighbor_index = i
        left_point = (point[my_index]+6) % 8
        right_point = (point[neighbor_index]+2) % 8

        if topni[my_index][left_point] != topni[neighbor_index][right_point]:
            change.append([neighbor_index, -1*cur_direction])
            cur_direction = -1*cur_direction
        else:
            break

    cur_direction = direction
    for i in range(target, 4): # 오른쪽 방향으로 탐색
        my_index = i-1
        neighbor_index = i
        right_point = (point[my_index]+2) % 8
        left_point = (point[neighbor_index]+6) % 8

        if topni[my_index][right_point] != topni[neighbor_index][left_point]:
            change.append([neighbor_index, -1*cur_direction])
            cur_direction = -1*cur_direction
        else:
            break

    for target_index, direction in change:
        if direction == 1:
            point[target_index] = (point[target_index]-1) % 8
        else:
            point[target_index] = (point[target_index]+1) % 8

ans = 0
for i in range(4):
    if topni[i][point[i]] == 1:
        ans += 2**(i)
print(ans)