import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
max_depth = 18

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [[0] * max_depth for _ in range(N+1)]
level = [0 for _ in range(N+1)]

def set_tree(node, pnode):
    parent[node][0] = pnode
    level[node] = level[pnode] + 1

    for child in graph[node]:
        if child == pnode: continue
        set_tree(child, node)

def set_parent():
    set_tree(1, 0)
    for i in range(1, max_depth):
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]


def lca(a, b):
    if level[a] > level[b]:
        a, b = b, a
    
    for i in range(max_depth-1, -1, -1):
        if level[b] - level[a] >= 2**i:
            b = parent[b][i]
    
    if a == b:
        return a
    
    for i in range(max_depth-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
            
    return parent[a][0]


set_parent()

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))