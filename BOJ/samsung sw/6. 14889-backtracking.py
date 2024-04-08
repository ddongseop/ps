import sys
input = sys.stdin.readline

N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

visited = [False for _ in range(N)]
minimum = 100000

def DFS(cnt, index):
    global minimum
    if cnt == N/2:
        A_ability = 0
        B_ability = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A_ability += ability[i][j]
                elif not visited[i] and not visited[j]:
                    B_ability += ability[i][j]
        minimum = min(abs(A_ability - B_ability), minimum)
        return
    for i in range(index, N):
        if not visited[i]:
            visited[i] = True
            DFS(cnt+1, i+1)
            visited[i] = False

DFS(0,0)
print(minimum)