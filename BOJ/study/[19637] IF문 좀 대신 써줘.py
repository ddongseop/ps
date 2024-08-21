import sys
input = sys.stdin.readline

N, M = map(int, input().split())

names = {}
uppers = []
for _ in range(N):
    name, upper = input().strip().split()
    if int(upper) in names: continue
    names[int(upper)] = name
    uppers.append(int(upper))

for _ in range(M):
    num = int(input())

    start, end = 0, len(uppers)-1
    while start <= end:
        mid = (start + end) // 2
        
        if num <= uppers[mid]:
            end = mid - 1
        else:
            start = mid + 1
        
    print(names[uppers[start]])