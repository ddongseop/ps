# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, K = map(int, input().split())
    nums = list(input())
    for i in range(len(nums)):
        if nums[i] == 'A': nums[i] = 10
        elif nums[i] == 'B': nums[i] = 11
        elif nums[i] == 'C': nums[i] = 12
        elif nums[i] == 'D': nums[i] = 13
        elif nums[i] == 'E': nums[i] = 14
        elif nums[i] == 'F': nums[i] = 15
        else: nums[i] = int(nums[i])

    slice_len = len(nums)//4

    candidates = []
    for _ in range(slice_len):
        candidates.append(nums[0:slice_len])
        candidates.append(nums[slice_len:2*slice_len])
        candidates.append(nums[2*slice_len:3*slice_len])
        candidates.append(nums[3*slice_len:4*slice_len])

        nums = deque(nums)
        nums.appendleft(nums.pop())
        nums = list(nums)

    answers = []
    for candidate in candidates:
        tmp = 1
        answer = 0
        for i in range(slice_len - 1, -1, -1):
            answer += candidate[i] * tmp
            tmp *= 16
        answers.append(answer)

    answers = list(set(answers))
    answers.sort(reverse=True)
    print("#{} {}".format(test_case, answers[K-1]))