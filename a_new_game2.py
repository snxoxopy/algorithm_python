import sys
from collections import deque
sys.stdin = open('input.txt','r')

n, k = map(int, input().split())

# 0은 흰색, 1은 빨간색, 2는 파란색이다.
arr = [list(map(int, input().split())) for _ in range(n)]
# r, c, d
info_horses = [list(map(int, input().split())) for _ in range(k)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]



def reverse_dir(dir):
    if dir % 2 == 0: return dir + 1
    else: return dir - 1



def get_game(k, arr, info_horses):
    n = len(arr)
    turn = 1
    stack_horses = [[[] for _ in range(n)] for _ in range(n)]

    for idx in range(k):
        [r, c, d] = info_horses[idx]
        r, c, d = r - 1, c - 1, d - 1
        info_horses[idx] = [r, c, d]
        stack_horses[r][c].append(idx)

    while turn <= 1000:
        for idx_horse in range(k):
            r, c, d = info_horses[idx_horse]
            nr, nc = r + dr[d], c + dc[d]

            if not -1 < nr < n or not -1 < nc < n or arr[nr][nc] == 2:
                nd = reverse_dir(d)
                info_horses[idx_horse][2] = nd
                nr, nc = r + dr[nd], c + dc[nd]

                if not -1 < nr < n or not -1 < nc < n or arr[nr][nc] == 2:
                    continue

            mv_idx_horse = []
            for i in range(len(stack_horses[r][c])):
                stack_idx_horse = stack_horses[r][c][i]
                if idx_horse == stack_idx_horse:
                    mv_idx_horse = stack_horses[r][c][i:]
                    stack_horses[r][c] = stack_horses[r][c][:i]
                    break

            if arr[nr][nc] == 1:
                mv_idx_horse = reversed(mv_idx_horse)

            for mv_idx in mv_idx_horse:
                stack_horses[nr][nc].append(mv_idx)
                info_horses[mv_idx][0], info_horses[mv_idx][1] = nr, nc

            if len(stack_horses[nr][nc]) >= 4: return turn

            #print(stack_horses)

        turn += 1

    return -1



print(get_game(k, arr, info_horses))


