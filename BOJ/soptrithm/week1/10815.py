import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

nums = sorted(nums)
ans = []
for target in targets:
    start = 0
    end = N-1

    while True:
        mid = (start + end) // 2
        if start > end:
            ans.append(0)
            break
        elif target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        elif target == nums[mid]:
            ans.append(1)
            break

print(*ans)