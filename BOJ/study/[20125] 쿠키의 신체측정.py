import sys
input = sys.stdin.readline

N = int(input())
field = []
for _ in range(N):
    field.append(list(input().rstrip()))

# 머리 찾기
head_x, head_y = -1, -1
for x in range(N): # 1000000 (백만)
    for y in range(N):
        if field[x][y] == '*':
            head_x, head_y = x, y
            break
    if head_x != -1 and head_y != -1: break

# 심장 위치 (머리 바로 아래)
heart_x, heart_y = head_x+1, head_y

# 왼쪽 팔 길이
left_arm = 0
for cur_y in range(heart_y-1, -1, -1): # 1000
    if field[heart_x][cur_y] == '*':
        left_arm += 1
    else:
        break

# 오른쪽 팔 길이
right_arm = 0
for cur_y in range(heart_y+1, N): # 1000
    if field[heart_x][cur_y] == '*':
        right_arm += 1
    else:
        break

# 몸통 끝점 찾기
body_x, body_y = heart_x, heart_y
body = 0
for cur_x in range(heart_x+1, N): # 1000
    if field[cur_x][body_y] == '*':
        body_x = cur_x
        body += 1
    else:
        break

left_leg = 0
for cur_x in range(body_x+1, N):
    if field[cur_x][body_y-1] == '*':
        left_leg += 1
    else:
        break

right_leg = 0
for cur_x in range(body_x+1, N):
    if field[cur_x][body_y+1] == '*':
        right_leg += 1
    else:
        break

print(heart_x+1, heart_y+1)
print(left_arm, right_arm, body, left_leg, right_leg)