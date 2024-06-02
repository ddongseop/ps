import sys
input = sys.stdin.readline

A, K = map(int, input().split())
dp = [0] * (K+1)
for tmp in range(A, K):
    if tmp + 1 <= K and dp[tmp+1] == 0:
        dp[tmp+1] = dp[tmp] + 1
    if tmp * 2 <= K and dp[tmp*2] == 0:
        dp[tmp*2] = dp[tmp] + 1

print(dp[K])