import sys
from copy import deepcopy
sys.stdin = open('input.txt', 'r')

# input
r, c, t = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(map(int, input().split())))

tmp_arr = []
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

# main
for _ in range(t):
    # 확산
    spread_dust()

    # 공기청소기 동작 - 반시계
    print('반시계')
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

# output
answer = sum(list(sum(arr, []))) + 2
print(answer)

