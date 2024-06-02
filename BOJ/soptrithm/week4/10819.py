import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
maximum = 0

def calculate_ans(nums):
    ans = 0
    for i in range(N-1):
        ans += abs(nums[i] - nums[i+1])
    return ans

def dfs(used, nums):
    global maximum

    if len(nums) == N:
        maximum = max(maximum, calculate_ans(nums))
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            dfs(used, nums+[A[i]])
            used[i] = False
    
dfs([False]*N, [])
print(maximum)