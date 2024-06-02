import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
sum_nums = sum(nums)
ans = 0

for num in nums:
    sum_nums -= num
    ans += sum_nums * num

print(ans)