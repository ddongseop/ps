import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
quest = list(map(int, input().split()))

nums = sorted(nums)
for i in range(M):
    start = 0
    end = N-1
    while True:
        mid = (start + end) // 2
        if start > end:
            print("0")
            break
        elif quest[i] < nums[mid]:
            end = mid - 1
        elif quest[i] > nums[mid]:
            start = mid + 1
        elif quest[i] == nums[mid]:
            print("1")
            break