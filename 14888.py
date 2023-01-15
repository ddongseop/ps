import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split())) # index 0: +, 1: -, 2: *, 3: //

maximum = -1000000000
minimum = 1000000000
def DFS(sum, cnt, operators):

    if cnt == N-1:
        global maximum
        global minimum

        if sum > maximum:
            maximum = sum
        if sum < minimum:
            minimum = sum
        
        return
    
    if operators[0]:
        operators[0] -= 1
        DFS(sum+nums[cnt+1], cnt+1, operators)
        operators[0] += 1
    
    if operators[1]:
        operators[1] -= 1
        DFS(sum-nums[cnt+1], cnt+1, operators)
        operators[1] += 1

    if operators[2]:
        operators[2] -= 1
        DFS(sum*nums[cnt+1], cnt+1, operators)
        operators[2] += 1

    if operators[3]:
        operators[3] -= 1
        DFS(int(sum/nums[cnt+1]), cnt+1, operators)
        operators[3] += 1

DFS(nums[0], 0, operators)
print(maximum)
print(minimum)