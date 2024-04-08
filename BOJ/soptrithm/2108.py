import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums = sorted(nums)

#산술평균 출력
mean = int(round(sum(nums)/N, 0))
print(mean)

#중앙값 출력
mid = N//2
print(nums[mid])

#최빈값 출력
tmp = Counter(nums).most_common()
maximum = tmp[0][1]
maximums = []

for n in tmp:
    if n[1] == maximum:
        maximums.append(n[0])

if len(maximums) > 1:
    maximums = sorted(maximums)
    print(maximums[1])
else:
    print(maximums[0])

#범위 출력
interval = nums[N-1] - nums[0]
print(interval)