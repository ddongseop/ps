import sys
input = sys.stdin.readline

N = int(input())
data = []
rates = []

for i in range(N):
    data.append(list(map(int, input().split())))    

for i in range(N):
    rate = 1
    for j in range(N):
        if i == j:
            continue
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rate += 1
    rates.append(rate)
        
for i in range(N-1):
    print(rates[i], end=" ")
print(rates[N-1])