import sys

sys.stdin = open('input.txt', 'r')

# input
r, c, t = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(map(int, input().split())))

#시간 초과의 이유로 사용하지 않음
#dr = [0, 1, 0, -1]
#dc = [1, 0, -1, 0]

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

# main
for _ in range(t):
    # 확산
    spread_dust()

    # 공기청소기 동작 - 반시계
    print('반시계')
    run_machine(pos_machine[0], -1)

    # 공기청소기 동작 - 시계
    print('시계')
    run_machine(pos_machine[1], 1)

# output
answer = sum(list(sum(arr, []))) + 2
print(answer)

