import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def top_down_dp(n, l):
    if l == 0:
        cnt = 1
    elif n == l:
        if dp[n-1][l-1] == -1:
            cnt = top_down_dp(n-1, l-1)
            cnt *= 2
        else:
            cnt = dp[n-1][l-1]
    else:
        if dp[n-1][l] == -1:
            cnt1 = top_down_dp(n-1, l)
        else:
            cnt1 = dp[n-1][l]
        if dp[n-1][l-1] == -1:
            cnt2 = top_down_dp(n-1, l-1)
        else:
            cnt2 = dp[n-1][l-1]
        cnt = cnt1 + cnt2
    
    dp[n][l] = cnt
    return cnt

def print_ans(n, l, i, cur):
    if l == 0:
        if cur < N:
            print(0, end='')
            print_ans(n, l, i, cur+1)
    elif n == l:
        if dp[n-1][l-1] < i:
            i -= dp[n-1][l-1]
            print(1, end='')
        else:
            print(0, end='')
        print_ans(n-1, l-1, i, cur+1)
    else:
        if dp[n-1][l] < i:
            i -= dp[n-1][l]
            print(1, end='')
            print_ans(n-1, l-1, i, cur+1)
        else:
            print(0, end='')
            print_ans(n-1, l, i, cur+1)

N, L, I = map(int, input().split())
dp = [[-1 for _ in range(L+1)] for _ in range(N+1)]
top_down_dp(N, L)
print_ans(N, L, I, 0)