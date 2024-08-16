import sys
input = sys.stdin.readline

# 이분탐색보다 이 풀이가 더 시간복잡도 낮음

N = int(input())
M = int(input())
positions = list(map(int, input().split()))

before = 0
ans = 0
for i in range(M):
    if before == 0:
        cur = 2 * positions[i]
    else: cur = positions[i] - before

    if cur > ans: ans = cur
    before = positions[i]

    if i == len(positions) - 1:
        cur = 2 * (N - positions[i])
        if cur > ans: ans = cur

if ans % 2 == 0:
    print(ans//2)
else:
    print(ans//2 + 1)