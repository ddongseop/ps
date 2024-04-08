import sys
input = sys.stdin.readline

def gcd(A, B):
    if A < B:
        A, B = B, A
    
    while B != 0:
        A, B = B, A % B
    
    return A

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print((A * B) // gcd(A, B))