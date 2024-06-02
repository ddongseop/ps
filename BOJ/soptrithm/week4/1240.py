import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    queue = deque()
    visited = [False] * (N+1)

    queue.append((start, 0))
    visited[start] = True

    while queue:
        cur, ans = queue.popleft()
        
        if cur == end:
            return ans
        
        for next, distance in graph[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append((next, ans+distance))
    
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, distance = map(int,input().split())
    graph[a].append((b, distance))
    graph[b].append((a, distance))

for _ in range(M):
    a, b = map(int,input().split())
    print(bfs(a, b))