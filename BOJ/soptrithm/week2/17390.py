import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = [0]*(N+1)

for i in range(N):
    B[i+1] = B[i] + A[i]

for _ in range(Q):
    start, end = map(int, input().split())
    print(B[end] - B[start-1])