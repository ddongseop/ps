import sys
input = sys.stdin.readline

M = int(input())
S = [0] * 20

for _ in range(M):
    command = input().split()

    if len(command) == 2:
        operation, num = command[0], int(command[1])

        if operation == 'add':
            S[num-1] = 1
        elif operation == 'remove':
            S[num-1] = 0
        elif operation == 'check':
            print(S[num-1])
        elif operation == 'toggle':
            S[num-1] = 1 - S[num-1]

    elif len(command) == 1:
        operation = command[0]
        
        if operation == 'all':
            S = [1] * 20
        elif operation == 'empty':
            S = [0] * 20