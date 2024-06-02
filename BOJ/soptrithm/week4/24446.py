import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
graph=[[] for _ in range(N+1)]

for _ in range(M):
    u, v =map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

visited=[False for _ in range(N+1)]
answer=[-1 for _ in range(N+1)]

def bfs(graph, start):
    queue=deque()
    depth = 0

    queue.append((start, depth))
    visited[start] = True
    answer[start]= depth

    while queue:
        current, depth = queue.popleft()
        answer[current]=depth
        
        for next in graph[current]:
            if not visited[next]:
                queue.append((next, depth+1))
                visited[next]=True

bfs(graph, R)
for i in range(1, N+1):
    print(answer[i])