import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = {}
for _ in range(N):
    word = input().strip()
    if len(word) < M: continue

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

ans = []
for key in words.keys():
    ans.append([-1 * words[key], -1 * len(key), key])

ans.sort()
for a in ans:
    print(a[2])