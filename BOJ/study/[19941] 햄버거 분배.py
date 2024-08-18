import sys
input = sys.stdin.readline

N, K = map(int, input().split())
string = input().strip()

hamburger = [False] * len(string)
person = []
for i in range(len(string)): # 20,000
    if string[i] == 'H':
        hamburger[i] = True
    if string[i] == 'P':
        person.append(i)

count = 0
for p in person: # 20,000
    start, end = p-K, p+K
    if p-K < 0: start = 0
    if p+K > len(string)-1: end = len(string)-1
    
    # p-K ~ p+K 에 햄버거가 있는지
    for i in range(start, end+1): # 10
        if hamburger[i] == True:
            hamburger[i] = False
            count += 1
            break

print(count)