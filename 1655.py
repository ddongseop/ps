import sys
input = sys.stdin.readline
import heapq

leftHeap = []
rightHeap = []
N = int(input())

for _ in range(N):
    num = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-num, num))
    else:
        heapq.heappush(rightHeap, (num, num))

    if rightHeap and leftHeap[0][1] > rightHeap[0][1]:
        r = heapq.heappop(rightHeap)[1]
        l = heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-r, r))
        heapq.heappush(rightHeap, (l, l))

    print(leftHeap[0][1])