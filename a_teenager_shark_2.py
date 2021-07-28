# https://www.acmicpc.net/problem/19236
# 문제 이해: 16분
# 구현:
# Debug: 35분
#   1) def fishes_move_1block(arr_fishes, r->cur_r, c->cur_c)
#   2) Load dir 순서 변경
#       AS-IS
#           for j in range(8):
#           dir_fish = arr_fishes[r][c][1]
#       TO-BE
#           dir_fish = arr_fishes[r][c][1]
#           for j in range(8):


import sys
import copy

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)
# 1 부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
#print(arr)
info_fish = [[None] * 4 for _ in range(4)]
# 다른 표현식 info_fish = [[[None] for _ in range(4)] for _ in range(4)]

# 물고기의 정보가 1번 행부터 순서대로 주어진다.
# ai는 물고기의 번호, bi는 방향

for i in range(4):
    for j in range(4):
        info_fish[i][j] = [arr[i][j*2], arr[i][j*2+1]-1]
#print(info_fish)

# 물고기 위치찾기
def find_pos_fishes(lst_2d, n):
    for i in range(4):
        for j in range(4):
            if lst_2d[i][j][0] == n: return (i, j)
    return None


# 물고기 이동
def fishes_move_1block(arr_fishes, cur_r, cur_c):
    for n_fish in range(1, 17):
        pos_fishes = find_pos_fishes(arr_fishes, n_fish)
        if pos_fishes is not None:
            r, c = pos_fishes[0], pos_fishes[1]
            dir_fish = arr_fishes[r][c][1]
            for j in range(8):
                nr, nc = r + dr[dir_fish], c + dc[dir_fish]

                if -1 < nr < 4 and -1 < nc < 4:
                    if not (nr == cur_r and nc == cur_c):
                        arr_fishes[r][c][1] = dir_fish
                        arr_fishes[r][c], arr_fishes[nr][nc] = arr_fishes[nr][nc], arr_fishes[r][c]
                        break #한 칸 이동이므로 이동 후 멈춤
                dir_fish = (dir_fish + 1) % 8



# 상어 이동
    # 가능 -> 물고기 존재: 방향 전환
    # 불가능 -> 물고기 없음: 집으로 돌아감

def get_shark_pos(arr, cur_r, cur_c):
    valid_pos = []
    dir_fish = arr[cur_r][cur_c][1]

    for i in range(4):
        cur_r += dr[dir_fish]
        cur_c += dc[dir_fish]
        if -1 < cur_r < 4 and -1 < cur_c < 4:
            if arr[cur_r][cur_c][0] != -1: valid_pos.append((cur_r, cur_c))
    return valid_pos


result = 0

# DFS 사용 -> 물고기 이동 후 상어가 이동하는 경우의 수(조합)을 탐색
def dfs(arr, cur_r, cur_c, tot):
    global result
    arr = copy.deepcopy(arr)

    tot += arr[cur_r][cur_c][0] # n_fish
    arr[cur_r][cur_c][0] = -1 # 먹은 물고기 -1
    fishes_move_1block(arr, cur_r, cur_c)
    valid_pos = get_shark_pos(arr, cur_r, cur_c)

    # 종료조건
    if len(valid_pos) == 0:
        result = max(result, tot)
        return

    # 수행
    for nr, nc in valid_pos:
        dfs(arr, nr, nc, tot)

dfs(info_fish, 0, 0, 0)
print(result)

