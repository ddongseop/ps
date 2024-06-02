import sys
input = sys.stdin.readline

N = int(input())
# dp = [0 for _ in range(N+1)]
# for tmp in range(2, N+1):
#     for minus in range(1, N//2+1):
#         A = tmp - minus
#         B = tmp - A
#         dp[tmp] = max(dp[tmp], dp[A]+dp[B]+(A*B))
# print(dp[N])
print(N*(N-1)//2)