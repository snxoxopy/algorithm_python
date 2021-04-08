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

def run_machine(rr, cc, dirr):  # 공기청정기 작동
    cp_arr = deepcopy(arr)
    if dirr == -1:
        rotate = ((0,1), (-1,0), (0,-1), (1,0))
    else:
        rotate = ((0,1), (1,0), (0,-1), (-1,0))

    for dr, dc in rotate:
        for _ in range(2*(r+c)-2):
            nr, nc = rr + dr, cc + dc
            if -1 < nr < r and -1 < nc < c and arr[nr][nc] == -1:  # 공기청정기의 오른쪽 값부터 시작해서 공기청정기를 만나면 종료한다.
                return cp_arr
            if -1 < nr < r and -1 < nc < c:
                cp_arr[nr][nc] = arr[rr][cc]
            else:
                break
            rr, cc = nr, nc


# main
for _ in range(t):
    # 확산
    spread_dust()

    # 공기청소기 동작 - 반시계
    print('반시계')
    print(arr)
    tmp_arr = run_machine(pos_machine[0], 1, -1)
    arr = deepcopy(tmp_arr)
    arr[pos_machine[0]][1] = 0
    print(arr)
    # 공기청소기 동작 - 시계
    print('시계')
    tmp_arr = run_machine(pos_machine[1], 1, 1)
    arr = deepcopy(tmp_arr)
    arr[pos_machine[1]][1] = 0

# output
answer = sum(list(sum(arr, []))) + 2
print(answer)

