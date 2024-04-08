import sys
input = sys.stdin.readline

N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

def combinations(pick, index, arr, new_arr, all_case):
    if len(new_arr) == pick:
        all_case.append(new_arr)
        return
    for i in range(index, len(arr)):
        combinations(pick, i+1, arr, new_arr + [arr[i]], all_case)

all_case = []
people = [i for i in range(N)]
combinations(N/2, 0, people, [], all_case)

minimum = 20000
for comb in all_case:
    team1 = comb
    team2 = list(set(people) - set(comb))

    two_case = []
    combinations(2, 0, team1, [], two_case)
    team1_ability = 0
    for case in two_case:
        i, j = case
        team1_ability += ability[i][j] + ability[j][i]

    two_case = []
    combinations(2, 0, team2, [], two_case)
    team2_ability = 0
    for case in two_case:
        i, j = case
        team2_ability += ability[i][j] + ability[j][i]

    minimum = min(abs(team2_ability - team1_ability), minimum)

print(minimum)