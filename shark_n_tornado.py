import sys

sys.stdin = open("input.txt", 'r')
n = int(input())
arr = []
for i in range(n): arr.append(list(map(int, input().split())))

# 현재 토네이토 위치
r, c = n // 2, n // 2

# 방향 벡터: 좌, 하, 우, 상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

# 모래 변화 비율
rate = [[0,0,2,0,0],
        [0,10,7,1,0],
        [5,'a',0,0,0],
        [0,10,7,1,0],
        [0,0,2,0,0]]


def shark_n_tornado(ans,board,rate,nx,ny):
    # rate (0,0)과 좌표 동기화 하기위함 offset 2
    a,b = nx-2, ny-2
    temp = 0 # nx, ny에서 빠져 나간 모래의 총 양
    for i in range(5):
        for j in range(5):
            if rate[i][j] != 'a' and rate[i][j] != 0:
                if -1 < i+a < n and -1 < j+b < n:
                    board[i+a][j+b] += board[nx][ny]*rate[i][j]//100
                else:
                    # 범위 안에 들어오지 않을 경우
                    ans += board[nx][ny]*rate[i][j]//100
                # a 자리에 모래를 채우기 위해서 빠져나가는 모래의 양을 temp 에 계속 더해준다.
                temp += board[nx][ny]*rate[i][j]//100
            # a 자리의 좌표를 기억
            elif rate[i][j] == 'a':
                remain = (i,j)
    # a = 비율이 적혀있는 칸으로 이동하지 않고 남은 모래의 양
    if -1 < remain[0]+a < n and -1 < remain[1]+b < n:
        board[remain[0]+a][remain[1]+b] += board[nx][ny] - temp
    else: # a 자리도 격자 바깥일 경우 격자 바깥으로 나가는 ans에 더해준다.
        ans += board[nx][ny] - temp
    # 토네이도가 지나간 자리는 0으로 초기화
    board[nx][ny] = 0
    return board, ans

def rot_rate(nrate):
    temp = [[0 for x in range(5)] for y in range(5)]
    for i in range(5):
        for j in range(5):
            temp[5 - j - 1][i] = nrate[i][j]
    return temp

ans, turn, flag = 0, 1, 1
nr, nc = r, c
while flag != 0:
    for d in range(4):
        for j in range(turn):
            nr, nc = nr + dr[d], nc + dc[d]
            if -1 < nr < n and -1 < nc < n:
                arr, ans = shark_n_tornado(ans, arr, rate, nr, nc)
            if (nr, nc) == (0, 0):
                flag = 0
            if d == 1 or d == 3:
                if j == 0: turn += 1  # 하, 상 이동 후 turn 증가
        rate = rot_rate(rate)
    if flag == 0:
        break
print(ans)

