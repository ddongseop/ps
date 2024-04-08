import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 2*N

done = [[False]*N for _ in range(N)]
# 가로 방향으로 먼저 테스트
for i in range(N):
    # 왼쪽부터 올라가보기    
    cur_height = board[i][0]
    signal = 0 # 1인 경우 경사로 놓기 실패
    candidates = [] # 0인 경우 왼쪽으로, 1인 경우 오른쪽으로 경사로 쌓기

    for j in range(1, N):
        if signal == 1:
            break

        if board[i][j] == cur_height: # 계속 평평할 경우 
           pass

        elif board[i][j]-cur_height == 1: # 1만 높아지는 경우
            if j < L: # 애초에 길이가 확보가 안되는 경우
                signal = 1
            else:
                candidates.append([0, j])
                for k in range(j-1, j-1-L, -1):
                    if board[i][k] != cur_height or done[i][k] == True:
                        signal = 1
                        break
                cur_height = board[i][j]

        elif cur_height - board[i][j] == 1: # 1만 낮아지는 경우
            if N-j < L: # 애초에 길이가 확보가 안되는 경우
                signal = 1
            else:
                candidates.append([1, j])
                for k in range(j, j+L):
                    if board[i][k] != cur_height-1 or done[i][k] == True:
                        signal = 1
                        break
                cur_height = board[i][j]

        else:
            signal = 1

    if signal == 0:
        for direction, j in candidates:
            if direction == 0:
                for k in range(j-1, j-1-L, -1):
                    if done[i][k] == True:
                        signal = 1
                        break
                    done[i][k] = True
            elif direction == 1:
                for k in range(j, j+L):
                    if done[i][k] == True:
                        signal = 1
                        break
                    done[i][k] = True

    if signal == 1:
        ans -= 1


done = [[False]*N for _ in range(N)]
# 세로 방향으로도 테스트
for i in range(N):
    # 아래쪽으로 내려가보기 올라가보기    
    cur_height = board[0][i]
    signal = 0 # 1인 경우 경사로 놓기 실패
    candidates = [] # 0인 경우 위쪽으로, 1인 경우 아래쪽으로 경사로 쌓기

    for j in range(1, N):
        if signal == 1:
            break

        if board[j][i] == cur_height: # 계속 평평할 경우 
           pass

        elif board[j][i]-cur_height == 1: # 1만 높아지는 경우
            if j < L: # 애초에 길이가 확보가 안되는 경우
                signal = 1
            else:
                candidates.append([0, j])
                for k in range(j-1, j-1-L, -1):
                    if board[k][i] != cur_height or done[k][i] == True:
                        signal = 1
                        break
                cur_height = board[j][i]

        elif cur_height - board[j][i] == 1: # 1만 낮아지는 경우
            if N-j < L: # 애초에 길이가 확보가 안되는 경우
                signal = 1
            else:
                candidates.append([1, j])
                for k in range(j, j+L):
                    if board[k][i] != cur_height-1 or done[k][i] == True:
                        signal = 1
                        break
                cur_height = board[j][i]
        else:
            signal = 1

    if signal == 0:
        for direction, j in candidates:
            if direction == 0:
                for k in range(j-1, j-1-L, -1):
                    if done[k][i] == True:
                        signal = 1
                        break
                    done[k][i] = True
            elif direction == 1:
                for k in range(j, j+L):
                    if done[k][i] == True:
                        signal = 1
                        break
                    done[k][i] = True

    if signal == 1:
        ans -= 1

print(ans)