import sys
input = sys.stdin.readline

N = int(input())
table = []
for _ in range(N):
    T, P = map(int, input().split())
    table.append([T, P])

maximum = 0
def DFS(price, cur):
    global maximum
    
    if cur == N+1:
        maximum = max(maximum, price)
        return
    
    if cur+table[cur-1][0] <= N+1:
        DFS(price+table[cur-1][1], cur+table[cur-1][0])
    
    if cur+1 <= N+1:
        DFS(price, cur+1)

    if cur+table[cur-1][0] > N+1:
        maximum = max(maximum, price)

DFS(0, 1)
print(maximum)