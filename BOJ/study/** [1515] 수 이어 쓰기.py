import sys
input = sys.stdin.readline

string = input().strip()
N = 1
cur = 0

while True: # 3,000
    count = 0
    for i in range(len(str(N))): # 30,000
        if count == 0 and str(N)[i] == string[cur]: 
            count = 1
            continue
        if count > 0:
            if cur + count >= len(string):
                break
            if str(N)[i] == string[cur + count]:
                count += 1
            ## 101에서 지우면 11이기 때문에 중간이 일치 안해도 포기하면 안됨

    if count > 0:
        cur += count
        if cur >= len(string): break
    N += 1

print(N)