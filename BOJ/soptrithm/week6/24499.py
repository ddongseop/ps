import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

A = A + A
acc = [0] * (2*N+1)
for i in range(1, 2*N+1):
    acc[i] = acc[i-1] + A[i-1]

ans = 0
for i in range(K, 2*N+1):
    ans = max(ans, acc[i] - acc[i-K])
print(ans)