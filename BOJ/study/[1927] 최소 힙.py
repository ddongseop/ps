import sys
input = sys.stdin.readline
import heapq

N = int(input())
queue = []
heapq.heapify(queue) # 반환값 없는 것 주의

for _ in range(N): # 100,000
    command = int(input())
    if command == 0 and len(queue) == 0:
        print(0)
    elif command == 0:
        print(heapq.heappop(queue)) # O(logN)
    else:
        heapq.heappush(queue, command) # O(logN)