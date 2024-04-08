import sys
input = sys.stdin.readline

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cctv = []
for i in range(N):
    for j in range(M):
        if office[i][j] >= 1 and office[i][j] <= 5:
            cctv.append([i, j])

def scan_right(office, cur_i, cur_j):
    changed = []
    for j in range(cur_j+1, M):
        if office[cur_i][j] == 6:
            break
        if office[cur_i][j] == 0:
            changed.append([cur_i, j])
            office[cur_i][j] = '#'
    return changed

def scan_left(office, cur_i, cur_j):
    changed = []
    for j in range(cur_j-1, -1, -1):
        if office[cur_i][j] == 6:
            break
        if office[cur_i][j] == 0:
            changed.append([cur_i, j])
            office[cur_i][j] = '#'
    return changed

def scan_bottom(office, cur_i, cur_j):
    changed = []
    for i in range(cur_i+1, N):
        if office[i][cur_j] == 6:
            break
        if office[i][cur_j] == 0:
            changed.append([i, cur_j])
            office[i][cur_j] = '#'
    return changed

def scan_up(office, cur_i, cur_j):
    changed = []
    for i in range(cur_i-1, -1, -1):
        if office[i][cur_j] == 6:
            break
        if office[i][cur_j] == 0:
            changed.append([i, cur_j])
            office[i][cur_j] = '#'
    return changed

minimum = N*M

def DFS(cnt, office):
    
    if cnt == len(cctv):
        cur_square = 0
        for i in range(N):
            for j in range(M):
                if office[i][j] == 0:
                    cur_square += 1
        global minimum
        minimum = min(minimum, cur_square)
        return
    
    cur_i, cur_j = cctv[cnt]
    cur_cctv = office[cur_i][cur_j]
    
    if cur_cctv == 1:
        changed = scan_right(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0
        
        changed = scan_left(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

        changed = scan_bottom(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

        changed = scan_up(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

    elif cur_cctv == 2:
        changed = scan_right(office, cur_i, cur_j) + scan_left(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

        changed = scan_bottom(office, cur_i, cur_j) + scan_up(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

    elif cur_cctv == 3:
        changed = scan_up(office, cur_i, cur_j) + scan_right(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

        changed = scan_right(office, cur_i, cur_j) + scan_bottom(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

        changed = scan_bottom(office, cur_i, cur_j) + scan_left(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

        changed = scan_left(office, cur_i, cur_j) + scan_up(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0
            
    elif cur_cctv == 4:
        changed = scan_up(office, cur_i, cur_j) + scan_right(office, cur_i, cur_j) + scan_left(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

        changed = scan_right(office, cur_i, cur_j) + scan_bottom(office, cur_i, cur_j) + scan_up(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

        changed = scan_bottom(office, cur_i, cur_j) + scan_left(office, cur_i, cur_j) + scan_right(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

        changed = scan_left(office, cur_i, cur_j) + scan_up(office, cur_i, cur_j) + scan_bottom(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

    elif cur_cctv == 5:
        changed = scan_up(office, cur_i, cur_j) + scan_right(office, cur_i, cur_j) + scan_left(office, cur_i, cur_j) + scan_bottom(office, cur_i, cur_j)
        DFS(cnt+1, office)
        for i, j in changed: office[i][j] = 0

DFS(0, office)
print(minimum)