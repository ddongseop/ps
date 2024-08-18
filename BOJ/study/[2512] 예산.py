import sys
input = sys.stdin.readline

N = int(input())
wants = list(map(int, input().split()))
M = int(input())

def cal_money(num):
    ans = 0
    for want in wants: # 10,000
        if want <= num:
            ans += want
        else:
            ans += num
    return ans

if sum(wants) <= M: # 10,000
    print(max(wants))
else:
    start, end = 0, 100000
    ans = 0
    while start <= end: # log(100,000) * 10,000
        mid = (start + end) // 2
        cur = cal_money(mid)

        if cur < M:
            if mid > ans: ans = mid
            start = mid + 1
        elif cur > M:
            end = mid - 1
        else:
            ans = mid
            break
    print(ans)