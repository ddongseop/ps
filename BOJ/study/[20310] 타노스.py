import sys
input = sys.stdin.readline

string = list(input().strip())

count_0 = 0
count_1 = 0
for s in string:
    if s == '0': count_0 += 1
    if s == '1': count_1 += 1

left_0 = count_0 // 2
cur = len(string)-1
while True:

    if string[cur] == '0':
        string.pop(cur)
        left_0 -= 1

    cur -= 1
    if left_0 == 0 or cur == -1: break

left_1 = count_1 // 2
cur = 0
while True:

    if string[cur] == '1':
        string.pop(cur)
        left_1 -= 1
    else: 
        cur += 1
    
    if left_1 == 0 or cur == len(string): break

ans = ''
for s in string:
    ans += s
print(ans)