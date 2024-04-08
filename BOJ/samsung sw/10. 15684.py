import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
line_left = {}
line_right = {}

for i in range(1, N+1):
    line_left[i] = []
    line_right[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    line_right[b].append(a)
    line_left[b+1].append(a)

def find_path(cur_n):
    for cur_h in range(1, H+1):
        if cur_h in line_right[cur_n]:
            cur_n += 1
        elif cur_h in line_left[cur_n]:
            cur_n -= 1
    return cur_n

def find_all_path():
    result = True
    for cur_n in range(1, N+1):
        if cur_n != find_path(cur_n):
            result = False
            break
    return result


ans = 4
def DFS(cnt, h):
    global ans
    if find_all_path() == True:
        ans = min(ans, cnt)
        return
    if cnt >= 3:
        return

    for cur_h in range(h, H+1):
        for cur_n in range(1, N):
            if cur_h not in line_right[cur_n] and cur_h not in line_left[cur_n] and cur_h not in line_right[cur_n+1]:
                line_right[cur_n].append(cur_h)
                line_left[cur_n+1].append(cur_h)
                DFS(cnt+1, cur_h)
                line_right[cur_n].pop()
                line_left[cur_n+1].pop()

DFS(0, 1)
if ans==4: ans = -1
print(ans)