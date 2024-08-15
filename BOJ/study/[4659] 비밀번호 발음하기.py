import sys
input = sys.stdin.readline

while True:
    password = input().strip()
    if password == 'end':
        break
    
    # 1번 조건 검증
    first_option = False
    for i in range(len(password)):
        if password[i] == 'a' or password[i] == 'e' or password[i] == 'i' or password[i] == 'o' or password[i] == 'u':
            first_option = True
    if first_option == False:
        print(f'<{password}> is not acceptable.')
        continue
    
    # 2번 조건 검증
    second_option = True
    is_current_vowel = False
    if password[0] == 'a' or password[0] == 'e' or password[0] == 'i' or password[0] == 'o' or password[0] == 'u':
        is_current_vowel = True
    count = 1
    for i in range(1, len(password)):
        if password[i] == 'a' or password[i] == 'e' or password[i] == 'i' or password[i] == 'o' or password[i] == 'u':
            if is_current_vowel == True:
                count += 1
            else:
                is_current_vowel = True
                count = 1

        else:
            if is_current_vowel == False:
                count += 1
            else:
                is_current_vowel = False
                count = 1
        if count >= 3:
            second_option = False
            break
    if second_option == False:
        print(f'<{password}> is not acceptable.')
        continue

    # 3번 조건 검증
    third_option = True
    cur_alpha = password[0]
    for i in range(1, len(password)):
        if cur_alpha != 'e' and cur_alpha != 'o' and password[i] == cur_alpha:
            third_option = False
        cur_alpha = password[i]
    if third_option == False:
        print(f'<{password}> is not acceptable.')
        continue

    print(f'<{password}> is acceptable.')