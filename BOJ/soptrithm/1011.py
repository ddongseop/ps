import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x

    cur_num = 1
    cur_ans = 1
    cur_size = 0
    
    while True:
        if cur_num > distance:
            cur_ans -= 1
            break
        elif cur_num == distance:
            break

        if cur_ans % 2 == 1:
            cur_ans += 1
            cur_size += 1
        
        elif cur_ans % 2 == 0:
            cur_ans += 1

        cur_num += cur_size

    print(cur_ans)