import sys

def hanoi_top(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi_top(n-1, start, 6-start-end)
    print(start, end)
    hanoi_top(n-1, 6-start-end, end)

N = int(input())
print(2**N-1)
hanoi_top(N, 1, 3)
