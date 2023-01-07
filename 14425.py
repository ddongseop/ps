import sys
input = sys.stdin.readline

N, M = map(int, input().split())
strings = set()
for _ in range(N):
    strings.add(input().strip())

cnt = 0
for _ in range(M):
    string = input().strip()
    if string in strings:
        cnt += 1

print(cnt)