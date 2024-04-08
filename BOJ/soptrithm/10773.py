import sys
input = sys.stdin.readline

K = int(input())
nums = [int(input()) for _ in range(K)]

ans = []
for num in nums:
    if num == 0:
        ans.pop()
    else:
        ans.append(num)

print(sum(ans))