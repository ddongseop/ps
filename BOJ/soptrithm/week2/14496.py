from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [[False]*(n+1) for _ in range(n+1)]
queue = deque([(a, 0)])

minimum = 10000
while queue:
    tmp, cur = queue.popleft()
    if tmp == b:
        if cur < minimum:
            minimum = cur
        continue

    for next in graph[tmp]:
        if visited[tmp][next]: continue
        visited[tmp][next] = True
        queue.append((next, cur+1))

if minimum == 10000:
    print(-1)
else:
    print(minimum)