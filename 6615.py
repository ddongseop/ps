import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    
    a_seq, b_seq = [A], [B]
    tmp_a, tmp_b = A, B
    while tmp_a != 1:
        if tmp_a % 2 == 0:
            tmp_a //= 2
        else:
            tmp_a = 3*tmp_a + 1
        a_seq.append(tmp_a)
    while tmp_b != 1:
        if tmp_b % 2 == 0:
            tmp_b //= 2
        else:
            tmp_b = 3*tmp_b + 1
        b_seq.append(tmp_b)
    
    a_cur, b_cur = len(a_seq)-1, len(b_seq)-1
    while a_cur > 0 and b_cur > 0:
        if a_seq[a_cur-1] != b_seq[b_cur-1]:
            break
        else:
            a_cur -= 1
            b_cur -= 1
    
    print(f'{A} needs {a_cur} steps, {B} needs {b_cur} steps, they meet at {a_seq[a_cur]}')

