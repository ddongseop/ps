import sys
input = sys.stdin.readline

N = int(input())
nums = set()
for _ in range(N):
    num = int(input())
    nums.add(num)

nums = sorted(list(nums))
for num in nums:
    print(num)