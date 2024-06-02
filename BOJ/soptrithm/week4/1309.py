import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(100001)]
dp[1], dp[2] = 3, 7

for i in range(3, N+1):
    dp[i] = (2*dp[i-1] + dp[i-2]) % 9901

print(dp[N])
