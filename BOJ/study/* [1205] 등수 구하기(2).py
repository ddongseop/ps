import sys
input = sys.stdin.readline

# 내림차순, 중복 값이 있을수도 있고 없을수도 있는 경우의 이분탐색
# 내림차순일 경우 등호 방향만 바뀜
# 중복 값이 있을 수 있는 경우에도 start로 밀고 나가기
def find_rate(scores, score):
    start, end = 0, len(scores)-1
    result = -1 # (추가)

    while start <= end:
        mid = (start + end) // 2
        if score > scores[mid]:
            end = mid - 1
        elif score < scores[mid]:
            start = mid + 1
        else: # score == scores[mid]
            result = mid # (추가) start 값 대신 result 활용
            end = mid - 1 # (추가) break 대신 계속 이어서 왼쪽으로 탐색
    
    if result == -1: # 중복 값이 없는 경우
        rate = start + 1
    else: # 중복 값이 있는 경우
        rate = result + 1

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