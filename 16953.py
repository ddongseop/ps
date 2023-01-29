import sys
input = sys.stdin.readline
from collections import deque

A, B = map(int, input().split())
queue = deque([(A, 1)])

while queue:
    tmp, cnt = queue.popleft()

    if tmp > B:
        continue
    if tmp == B:
        print(cnt)
        break

    queue.append((int(str(tmp)+"1"), cnt+1))
    queue.append((2*tmp, cnt+1))
else:
    print(-1)

# Point1: 오른쪽에 1 추가하는거는 10만 곱하는거 아님
# Point2: cnt 그냥 queue에 같이 넣으면 됨
# Point3: while ~ else문도 존재함
# Point4: visited 사용할 필요 없음
# Point5: 그리디로 풀수도 있음

# A, B = map(int, input().split())
# cnt = 1
# while B != A:
#     cnt += 1
#     tmp = B
#     if B % 10 == 1:
#         B //= 10
#     elif B % 2 == 0:
#         B //= 2
    
#     if tmp == B:
#         print(-1)
#         break
# else:
#     print(cnt)