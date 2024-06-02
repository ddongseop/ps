import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
question = [int(input()) for _ in range(M)]

nums.sort()

for q in question:

    start = 0
    end = N-1
    ans = -1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == q:
            if end == mid:
                ans = mid
                break
            end = mid
        
        elif nums[mid] > q:
            end = mid-1
        else:
            start = mid+1
    
    print(ans)