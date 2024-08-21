import sys
input = sys.stdin.readline

# k개의 문제 -> 0~100점 
# 팀 ID, 문제 번호, 점수
# 점수 중 최고 점수가 최종 점수, 한번도 안냈으면 0
# 팀의 최종 점수 = 최종 점수의 합

# 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다
# 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())

    score = [[0]*k for _ in range(n)]  # [팀 번호][문제 번호]
    submit = [0]*n
    last = [0]*n

    for sec in range(m): # 10,000
        i, j, s = map(int, input().split())

        if s > score[i-1][j-1]: score[i-1][j-1] = s
        submit[i-1] += 1
        last[i-1] = sec

    total = []
    for team in range(n): # 100
        total.append([-1 * sum(score[team]), submit[team], last[team], team])
    total.sort()

    for i in range(n): # 100
        if total[i][3] == t-1:
            print(i+1)
            break