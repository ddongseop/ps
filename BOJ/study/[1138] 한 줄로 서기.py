import sys
input = sys.stdin.readline

# 종이에 적어보며 그리디라는 것을 깨달음

N = int(input())
counts = list(map(int, input().split()))

ans = [-1] * N
avail = [i for i in range(N)]

for i in range(1, N+1):
    count = counts[i-1]
    ans[avail[count]] = i
    del avail[count]

print(*ans)