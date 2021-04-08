import sys
<<<<<<< HEAD
from copy import deepcopy
=======

>>>>>>> 45dc6b3e15701ce208120eeb7d7cba3f5c18b034
sys.stdin = open('input.txt', 'r')

# input
r, c, t = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(map(int, input().split())))

<<<<<<< HEAD
tmp_arr = []
=======
#시간 초과의 이유로 사용하지 않음
#dr = [0, 1, 0, -1]
#dc = [1, 0, -1, 0]

>>>>>>> 45dc6b3e15701ce208120eeb7d7cba3f5c18b034
pos_machine = []

# system

for i in range(r):
    if arr[i][0] == -1:
        pos_machine.append(i)

def spread_dust(): #확산1
    tmp_dust = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            dust = arr[i][j]
            if dust > 0:
                cnt = 0
                for dr, dc in (-1,0), (1,0), (0,1), (0,-1):
                    nr, nc = i + dr, j + dc
                    if -1 < nr < r and -1 < nc < c and arr[nr][nc] != -1:
                        cnt += 1
                        tmp_dust[nr][nc] += dust // 5
                arr[i][j] = dust - dust // 5 * cnt

    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_dust[i][j] # arr[i][j] = arr[i][j] + tmp_dust[i][j]

# def spread_dust(): #확산2
#     tmp_dust = [[0] * c for _ in range(r)]
#     for i in range(r):
#         for j in range(c):
#             if arr[i][j] >= 5:
#                 div5 = arr[i][j]//5
#                 for dr, dc in (-1,0), (1,0), (0,1), (0,-1):
#                     nr, nc = i + dr, j + dc
#                     if 0 <= nr < r and 0 <= nc < c and arr[nr][nc] != -1:
#                         tmp_dust[nr][nc] += div5
#                         arr[i][j] -= div5
#     for i in range(r):
#         for j in range(c):
#             arr[i][j] += tmp_dust[i][j]

<<<<<<< HEAD
def run_machine(rr, cc, diff):  # 공기청정기 작동
        cp_arr = deepcopy(arr)
        dr = (1, -1, 0, 0)
        dc = (0, 0, 1, -1)
        for d in diff:
            while True:  # 공기청정기의 오른쪽 값부터 시작해서 공기청정기를 만나면 종료한다.
                nr, nc = rr + dr[d], cc + dc[d]
                if -1 < nr < r and -1 < nc < c and arr[nr][nc] == -1:
                    return cp_arr
                if -1 < nr < r and -1 < nc < c:
                    #print(nr, nc)
                    cp_arr[nr][nc] = arr[rr][cc]
                else:
                    break
                rr, cc = nr, nc
                #print(cp_arr)
=======
def run_machine(start, dir):
    if dir == -1: # 공기청소기 동작 - 반시계
        for i in range(start - 1, 0, -1):
            arr[i][0] = arr[i-1][0]
        for j in range(0, c-1):
            arr[0][j] = arr[0][j+1]
        for i in range(0, start):
            arr[i][c-1] = arr[i+1][c-1]
        for j in range(c-1, 1, -1):
            arr[start][j] = arr[start][j-1]
    else: # 공기청소기 동작 - 시계
        for i in range(start + 1, r - 1):
            arr[i][0] = arr[i + 1][0]
        for j in range(0, c - 1):
            arr[r - 1][j] = arr[r - 1][j + 1]
        for i in range(r - 1, start, -1):
            arr[i][c - 1] = arr[i - 1][c - 1]
        for j in range(c - 1, 1, -1):
            arr[start][j] = arr[start][j - 1]
    arr[start][1] = 0
>>>>>>> 45dc6b3e15701ce208120eeb7d7cba3f5c18b034

# main
for _ in range(t):
    # 확산
    spread_dust()

    # 공기청소기 동작 - 반시계
    print('반시계')
<<<<<<< HEAD
    print(arr)
    tmp_arr = run_machine(pos_machine[0], 1, (2, 1, 3, 0))
    arr = deepcopy(tmp_arr)
    arr[pos_machine[0]][1] = 0
    print(arr)
    # 공기청소기 동작 - 시계
    print('시계')
    tmp_arr = run_machine(pos_machine[1], 1, (2, 0, 3, 1))
    arr = deepcopy(tmp_arr)
    arr[pos_machine[1]][1] = 0
=======
    run_machine(pos_machine[0], -1)

    # 공기청소기 동작 - 시계
    print('시계')
    run_machine(pos_machine[1], 1)
>>>>>>> 45dc6b3e15701ce208120eeb7d7cba3f5c18b034

# output
answer = sum(list(sum(arr, []))) + 2
print(answer)

