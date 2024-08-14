import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N): #50
    weight, height = map(int, input().split())
    info.append([weight, height])

# N이 작기 때문에 브루트포스
ans = []
for me in range(N): #50
    rate = 1
    my_weight, my_height = info[me][0], info[me][1]

    for other in range(N): #50
        if me == other: # 괜히 이거 안뺴려고 하지 말기
            continue
        other_weight, other_height = info[other][0], info[other][1]

        if other_weight > my_weight and other_height > my_height:
            rate += 1
            
    ans.append(rate)

print(*ans)