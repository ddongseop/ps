import sys
input = sys.stdin.readline

N = int(input())
lengths = list(map(int, input().split())) # N-1
costs = list(map(int, input().split())) # N

pos_costs = []
for i in range(len(costs)): # 100,000
    pos_costs.append([costs[i], i])
pos_costs.sort() # 100,000 * 17

ans = 0
start = N
for i in range(len(pos_costs)): # 100,000
    cur_cost, cur_pos = pos_costs[i][0], pos_costs[i][1]
    if cur_pos >= start: continue

    ans += cur_cost * sum(lengths[cur_pos:start])
    start = cur_pos

    if start == 0:
        break

print(ans)