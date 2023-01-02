import sys
input = sys.stdin.readline
import heapq

N = int(input())
clss = []
for _ in range(N):
    S, T = map(int, input().split())
    clss.append([S, T])

clss.sort()

room = []
heapq.heappush(room, clss[0][1])

for i in range(1, N):
    if clss[i][0] < room[0]:
        heapq.heappush(room, clss[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, clss[i][1])

print(len(room))