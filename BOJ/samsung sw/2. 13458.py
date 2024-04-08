import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = len(A)
for a in A:
    a -= B
    if a > 0:
        ans += a // C
        if a % C:
            ans += 1

print(ans)