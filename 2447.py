import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def fillStar(n):
    if n == 1:
        return ['*']

    stars = fillStar(n//3) 
    
    ans = []  
    for star in stars:
        ans.append(star*3)
    for star in stars:
        ans.append(star+' '*(n//3)+star)
    for star in stars:
        ans.append(star*3)
    return ans

N = int(input())
print('\n'.join(fillStar(N)))