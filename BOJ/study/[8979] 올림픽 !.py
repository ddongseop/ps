import sys
input = sys.stdin.readline

N, K = map(int, input().split())

info = []
for _ in range(N): # 1000
    num, gold, silver, bronze = map(int, input().split())
    info.append([gold, silver, bronze, num])
info.sort(reverse=True) # 3000 # 기본은 오름차순이라는 것 주의

for i in range(N): #1000 * 1000
    if K == info[i][3]:
        ans = i
        for cur in range(i, -1, -1): 
            if info[cur][0] == info[i][0] and info[cur][1] == info[i][1] and info[cur][2] == info[i][2]:
                ans = cur
            else:
                break
        break

print(ans+1)