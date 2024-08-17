import sys
input = sys.stdin.readline

P = int(input())

# 이분 탐색으로도 풀 수 있음
# 오름차순, 중복 값이 없는 경우의 이분탐색
def find_index(cur, row):
    start, end = 0, len(row)-1

    while start <= end:
        mid = (start + end) // 2

        if cur < row[mid]:
            end = mid - 1
        elif cur > row[mid]:
            start = mid + 1

    return start

for case in range(1, P+1):
    heights = list(map(int, input().split()))
    row = []
    count = 0

    for i in range(1, 21):
        cur = heights[i]
        if len(row) == 0 or row[-1] < cur:
            row.append(cur)
        else:
            index = find_index(cur, row)
            count += len(row) - index
            row = row[0:index] + [cur] + row[index:]

    print(case, count)