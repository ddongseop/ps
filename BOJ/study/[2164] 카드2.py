import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
Q =  deque([i for i in range(1, N+1)])

while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())

print(Q[0])