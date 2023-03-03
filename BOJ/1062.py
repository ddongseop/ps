import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if K < 5:
    print(0)
    exit()

elif K == 26:
    print(N)
    exit()

ans = 0
words = [set(input().strip()) for _ in range(N)]
learn = [0] * 26

for a in ('a', 'c', 'i', 'n', 't'):
    learn[ord(a) - ord('a')] = 1

def dfs(start, learned):
    global ans

    if learned == K-5:
        cnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                cnt += 1
        ans = max(ans, cnt)
        return

    for i in range(start, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(i, learned + 1)
            learn[i] = 0

dfs(0, 0)
print(ans)