import sys
import copy
sys.setrecursionlimit(10**6)

#input
sys.stdin = open('input.txt','r')
data = []
for _ in range(4): data.append(list(map(int, input().split())))

#arr[r][c][0] = 물고기 번호, arr[r][c][1] = 방향
arr = [[[None] for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4): arr[i][j] = [data[i][j*2], data[i][j*2+1]-1]

#물고기가 이동할 수 있는 방향 정의
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
answer = 0

def find_pos(arr, idx_fish):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == idx_fish:
                return (i, j)
    return None

def mv_all_fishes(arr, cur_r, cur_c):
    # fishes for i in range(1, 17):
    for idx_fish in range(1, 17):
        # if not pos_shark = if find_pos_fishes -> (nr, nc)
        pos_fish = find_pos(arr, idx_fish)
        if pos_fish != None:
            r, c = pos_fish[0], pos_fish[1]
            dir = arr[r][c][1]
            # for d in range(8): 45도 회전
            for d in range(8):
                nr = r + dr[dir]
                nc = c + dc[dir]
                #  -1 < r < 4 and -1 < c < 4: 물고기 이동가능
                if -1 < nr < 4 and -1 < nc < 4:
                    if not (nr == cur_r and nc == cur_r):
                        arr[r][c][1] = dir
                        arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
                        break
                dir = (dir + 1) % 8

def mv_shark(arr, r, c):
    pos_shark = []
    dir = arr[r][c][1]
    for _ in range(4):
        r += dr[dir]
        c += dc[dir]
        if -1 < r < 4 and -1 < c < 4:
            if arr[r][c][0] != -1: pos_shark.append((r, c))
    return pos_shark

def dfs(arr, r, c, had_fishes):
    global answer
    arr = copy.deepcopy(arr)
    # 최초 상어이동
    had_fishes += arr[r][c][0]
    arr[r][c][0] = -1

    # 물고기 이동
    mv_all_fishes(arr, r, c)

    # 상어 이동 가능 경우의 수 뽑아내기
    pos_shark = mv_shark(arr, r, c)

    # 종료조건
    if len(pos_shark) == 0:
        answer = max(answer, had_fishes)
        return
    for nr, nc in pos_shark:
        dfs(arr, nr, nc, had_fishes)


#main -> output
dfs(arr, 0, 0, 0)
print(answer)