import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

def dfs(start, end):

    if start > end:
        return
    
    tmp = end + 1
    for i in range(start + 1, end + 1): # start는 어짜피 루트니깐, start+1부터 시작 / end 알아서 len-1로 들어오니까 end+1까지로 세팅
        if tree[i] > tree[start]:
            tmp = i # 서브트리들로 나눠지는 지점 체크
            break
    
    dfs(start + 1, tmp - 1) # 왼쪽 서브트리 재귀로 탐색
    dfs(tmp, end) # 오른쪽 서브트리 재귀로 탐색

    print(tree[start])


tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

dfs(0, len(tree) - 1)