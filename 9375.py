import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    wear_cnt = {}
    for _ in range(N):
        name, category = input().split()
        if category in wear_cnt:
            wear_cnt[category] += 1
        else:
            wear_cnt[category] = 1
    
    ans = 1
    for category in wear_cnt:
        ans *= wear_cnt[category] + 1
    print(ans - 1)