import sys
input = sys.stdin.readline

dp = [[0]*14 for _ in range(15)]
dp[0] = [i for i in range(1, 15)]
for k in range(1, 15):
    dp[k][0] = dp[k-1][0]
    for n in range(1, 14):
        dp[k][n] = dp[k][n-1] + dp[k-1][n]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])