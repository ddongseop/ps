import sys
input = sys.stdin.readline

N = int(input())
switch = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    gender, num = map(int, input().split())
    if gender == 1:
        cur = num
        while cur <= len(switch):
            switch[cur-1] = 1 - switch[cur-1]
            cur += num
    else:
        switch[num-1] = 1 - switch[num-1]
        left = num-1
        right = num+1
        while left > 0 and right <= len(switch):
            if switch[left-1] != switch[right-1]:
                break
            switch[left-1] = 1 - switch[left-1]
            switch[right-1] = 1 - switch[right-1]

            left -= 1
            right += 1

for i in range(1, len(switch)+1):
    print(switch[i-1], end=" ")
    if i % 20 == 0:
        print()
print()