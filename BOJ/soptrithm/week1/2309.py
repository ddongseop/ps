import sys
input = sys.stdin.readline

height = sorted([int(input()) for _ in range(9)])

def DFS(index, picked):
    if len(picked) == 7:
        sum = 0
        for p in picked: sum += height[p]
        if sum == 100:
            for p in picked:
                print(height[p])
            exit(0)
        else:
            return

    for i in range(index, 9):
        picked.append(i)
        DFS(i+1, picked)
        picked.pop()

DFS(0, [])