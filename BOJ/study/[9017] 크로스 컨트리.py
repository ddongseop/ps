import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    
    count = {}
    for num in nums: # 1000
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    score = {}
    for num in list(count.keys()): # 200
        score[num] = []

    rate = 1
    for num in nums: #1000
        if count[num] < 6:
            continue
        score[num].append(rate)
        rate += 1

    ans = []
    for num in list(count.keys()): # 200
        if count[num] < 6:
            continue
        ans.append([sum(score[num][:4]), score[num][4], num])
    
    ans.sort() # 200log200
    print(ans[0][2])