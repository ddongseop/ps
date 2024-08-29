import sys
input = sys.stdin.readline

N, M = map(int, input().split())

keywords = {}
for _ in range(N): # 2 x 10^5
    keyword = input().strip()
    keywords[keyword] = True

count = N
for _ in range(M): # 2 x 10^5
    used = list(input().rstrip().split(','))
    for u in used: # 10
        # u in keywords : O(1)
        if u in keywords and keywords[u] == True:
            count -= 1
            keywords[u] = False

    print(count)