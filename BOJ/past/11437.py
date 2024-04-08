import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def set_tree(node, pnode):
    parent[node] = pnode
    level[node] = level[pnode] + 1

    for child in graph[node]:
        if child == pnode: continue
        set_tree(child, node)

def lca(a, b):
    if level[a] < level[b]:
        tmp = a
        a = b
        b = tmp
    
    while level[a] != level[b]:
        a = parent[a]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0 for _ in range(N+1)]
level = [0 for _ in range(N+1)]
set_tree(1, 0)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(f'{lca(a, b)}')