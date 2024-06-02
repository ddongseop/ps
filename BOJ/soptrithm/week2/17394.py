import sys, math
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
	
    prime = [1 for _ in range(B+1)]
    prime[1] = 0
    for i in range(2, int(math.sqrt(B))+1):
        if prime[i] == 1:
            j = 2
            while i*j <= B:
                prime[i*j] = 0
                j += 1

    candidates = []
    for i in range(A, B+1):
        if prime[i]:
            candidates.append(i)
    
    if len(candidates) == 0:
        print(-1)
        continue

    queue = deque([(0, N)])
    visited = [False]*5000001
    visited[N] = True
    while queue:
        snap, num = queue.popleft()
        if num in candidates:
            print(snap)
            break

        if not visited[num//2]:
            queue.append((snap+1, num//2))
            visited[num//2] = True
        
        if not visited[num//3]:
            queue.append((snap+1, num//3))
            visited[num//3] = True

        if not visited[num+1]:
            queue.append((snap+1, num+1))
            visited[num+1] = True
        
        if num > 0 and not visited[num-1]:
            queue.append((snap+1, num-1))
            visited[num-1] = True