import sys
input = sys.stdin.readline
from collections import defaultdict

M, N = map(int, input().split())
universe = defaultdict(int)
for _ in range(M):
    planets = list(map(int, input().split()))
    _planets = sorted(list(set(planets)))
    index = {_planets[i]: i for i in range(len(_planets))}
    zip = tuple([index[x] for x in planets])
    universe[zip] += 1

ans = 0
for cnt in universe.values():
    ans += cnt * (cnt - 1) // 2
print(ans)