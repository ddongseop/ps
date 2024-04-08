import sys
input = sys.stdin.readline
import heapq

array = []
N = int(input())
for _ in range(N):
    x = int(input())
    
    if x == 0 and array:
        tmp = heapq.heappop(array)
        print(tmp[1])
        
    elif x == 0 and not array:
        print(0)

    elif x < 0:
        heapq.heappush(array, (-1*x, x))
    
    else:
        heapq.heappush(array, (x, x))
