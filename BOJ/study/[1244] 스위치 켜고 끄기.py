import sys
input = sys.stdin.readline

N = int(input())
switch = list(map(int, input().split()))
P = int(input())
for _ in range(P):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(1, len(switch)//num + 1):
            switch[num*i-1] = 1 - switch[num*i-1]
    else:
        switch[num-1] = 1 - switch[num-1]
        cur = 1
        while (num-1+cur) <= len(switch)-1 and (num-1-cur) >= 0:
            if switch[num-1+cur] == switch[num-1-cur]:
                switch[num-1+cur] = 1 - switch[num-1+cur]
                switch[num-1-cur] = 1 - switch[num-1-cur]
            else:
                break
            cur += 1

for i in range(0, len(switch)):
    if i != 0 and i % 20 == 0:
        print()
    print(switch[i], end="")
    if (i+1) % 20 != 0:
        print(" ", end="")
# 마지막에 % 출력 방지
print()