import sys
input = sys.stdin.readline

N = int(input())
original = input().strip()
count = 0

for _ in range(N-1): #100
    string = input().strip()

    if len(original) == len(string): # 두 문자의 길이가 같을 경우

        checked = [0]*len(original)
        for s in string: #100
            for i in range(len(original)):
                if s == original[i] and checked[i] == 0:
                    checked[i] = 1
                    break
        
        if sum(checked) >= len(original) - 1:
            count += 1

    elif len(original) == len(string) + 1: # 한 문자를 더해야 같아질 경우

        checked = [0]*len(original)
        for s in string: #100
            for i in range(len(original)):
                if s == original[i] and checked[i] == 0:
                    checked[i] = 1
                    break
        
        if sum(checked) == len(original) - 1:
            count += 1

    elif len(original) == len(string) - 1: # 한 문자를 빼야 같아질 경우

        checked = [0]*len(original)
        for s in string: #100
            for i in range(len(original)):
                if s == original[i] and checked[i] == 0:
                    checked[i] = 1
                    break
        if sum(checked) == len(original):
            count += 1

print(count)