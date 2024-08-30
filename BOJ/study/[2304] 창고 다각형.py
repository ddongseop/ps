import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
field = []
max_height = 0

for _ in range(N): # 1,000
    L, H = map(int, input().split())
    field.append((L, H))
    if H > max_height:
        max_height = H
field = deque(sorted(field))

ans = 0
before_height = field[0][1]
before_pos = field[0][0]
reversed = False

while True: # 1,000

    cur_pos, cur_height = field.popleft()
    
    if cur_height > before_height:
        ans += before_height * abs(cur_pos - before_pos)

        before_height = cur_height
        before_pos = cur_pos
    
    if cur_height == max_height and reversed == True:
        field.appendleft((cur_pos, cur_height))
        break
    if cur_height == max_height and reversed == False:
        field.appendleft((cur_pos, cur_height))
        field.reverse()
        reversed = True
        before_height = field[0][1]
        before_pos = field[0][0]

ans += max_height * (abs(field[0][0] - field[-1][0]) + 1)
print(ans)