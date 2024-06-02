import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
answer = 0

def dfs(length, num):
    global answer
    for i in range(3):
        if length==0 and i==0:
            continue
        if length == N:
            if num % 3 == 0:
                answer += 1
            return
        else:
            dfs(length+1, int(str(num+i)))

dfs(0, 0)
print(answer)