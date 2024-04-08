import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_val = -int(1e9)
min_val = int(1e9)

def DFS(sum, cnt, plus, minus, mul, div):

    if cnt == N-1:
        global max_val
        global min_val
        if sum > max_val:
            max_val = sum
        if sum < min_val:
            min_val = sum
        return
    
    if plus:
        DFS(sum+A[cnt+1], cnt+1, plus-1, minus, mul, div)
    if minus:
        DFS(sum-A[cnt+1], cnt+1, plus, minus-1, mul, div)
    if mul:
        DFS(sum*A[cnt+1], cnt+1, plus, minus, mul-1, div)
    if div:
        DFS(int(sum/A[cnt+1]), cnt+1, plus, minus, mul, div-1)

DFS(A[0], 0, operators[0], operators[1], operators[2], operators[3])
print(max_val)
print(min_val)