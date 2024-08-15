import sys
input = sys.stdin.readline

N, game = input().strip().split()
N = int(N)

names = set()
for _ in range(N):
    name = input().strip()
    names.add(name)

if game == 'Y':
    print(len(names))

if game == 'F':
    print(len(names)//2)

if game == 'O':
    print(len(names)//3)