import sys
input = sys.stdin.readline
import heapq

# 12MB = 12 * 1024 * 1024 Byte = 12,582,912
# int는 24 Byte
# 대략적으로 500,000 개 정도만 저장 가능
# 1500 * 1500은 2,250,000이므로 불가능

N = int(input())
heap = []

for _ in range(N): # 1,500
    nums = list(map(int, input().split()))
    for num in nums:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heapq.heappop(heap))