import sys
input = sys.stdin.readline

X = int(input())
piece = [64, 32, 16, 8, 4, 2, 1]
cnt = 0
for i in range(len(piece)):
    if piece[i] > X:
        continue
    else:
        X -= piece[i]
        cnt += 1
print(cnt)