import sys
input = sys.stdin.readline

def binary_search(li, target):
    start = 0 
    end = len(li)-1
    ans = -1

    while start <= end:
        mid = (start + end) // 2
        if li[mid] < target:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    cnt = 0
    for a in A:
        cnt += binary_search(B, a) + 1
    print(cnt)