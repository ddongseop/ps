import sys
input = sys.stdin.readline

N, X = map(int, input().split())
counts = list(map(int, input().split()))

cumulate = [counts[0]]
for i in range(1, N): # 250,000
    cumulate.append(cumulate[i-1] + counts[i])

ans = 0
duplicate = 0
for start in range(N-(X-1)): # 250,000
    end = start + (X-1)
    # cur = sum(counts[start:end+1])
    cur = cumulate[end] - cumulate[start] + counts[start]
    if cur > ans:
        ans = cur
        duplicate = 1
    elif cur == ans:
        duplicate += 1
    
if ans == 0:
    print("SAD")
else:
    print(ans)
    print(duplicate)