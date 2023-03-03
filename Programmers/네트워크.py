from collections import deque

def solution(n, computers):
    visited = [False] * n
    count = 0
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        count += 1
        
        queue = deque()
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == False:
                queue.append(j)
        while queue:
            tmp = queue.popleft()
            visited[tmp] = True
            for j in range(n):
                if computers[tmp][j] == 1 and visited[j] == False:
                    queue.append(j)
    
    return count