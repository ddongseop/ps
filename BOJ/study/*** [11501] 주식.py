import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    prices.reverse() # 이거 생각 못했음

    profit = 0
    high = prices[0]

    for i in range(1, N): # 1,000,000
        if prices[i] < high:
            profit += (high - prices[i])
        elif prices[i] > high:
            high = prices[i]

    print(profit)