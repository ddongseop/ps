import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())

ans = 0
while A != B:
    A -= A // 2
    B -= B // 2
    ans += 1
print(ans)