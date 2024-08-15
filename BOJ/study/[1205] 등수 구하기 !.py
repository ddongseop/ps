import sys
input = sys.stdin.readline

# 내림차순일 경우 등호 방향만 바뀜
# 중복 값이 있을 수 있는 경우에도 start로 밀고 나가기
def find_rate(scores, score):
    start, end = 0, len(scores)-1

    while start <= end:
        mid = (start + end) // 2
        if score > scores[mid]:
            end = mid - 1
        elif score < scores[mid]:
            start = mid + 1
        else:
            start = mid
            break
    
    rate = start + 1
    for i in range(start-1, -1, -1):
        if score == scores[i]:
            rate -= 1
    return rate

N, score, P = map(int, input().split())
if N > 0:
    scores = list(map(int, input().split()))
    if len(scores) == P and scores[-1] >= score:
        print(-1)
    else:
        print(find_rate(scores, score))
else:
    print(1)