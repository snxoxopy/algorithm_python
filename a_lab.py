import sys, copy
from collections import deque

sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, -0]
q_pos_virus = deque()
minV = m*n
cntW = 0

# 벽의 개수와 바이러스의 위치 저장
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1: cntW += 1
        elif arr[i][j] == 2: q_pos_virus.append([i, j])


# 바이러스 퍼뜨리기
def spread_vs(tmp_arr, tmp_pos_virus):
    global minV
    res = len(tmp_pos_virus)
    while tmp_pos_virus:
        #if res > minV: return minV -> 약간의 시간 감소
        r, c = tmp_pos_virus.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if -1 < nr < n and -1 < nc < m:
                if tmp_arr[nr][nc] == 0:
                    tmp_arr[nr][nc] = 2
                    tmp_pos_virus.append([nr, nc])
                    res += 1
    return res


# 3가지 조합 선택 후 벽 세우기
def build_walls(cnt_walls, x, y):
    global minV
    if cnt_walls == 3:
        cmb_walls = copy.deepcopy(arr)
        pos_virus = copy.deepcopy(q_pos_virus)
        result = spread_vs(cmb_walls, pos_virus)
        if result < minV: minV = result
        return
    else:
        # 이 부분 처리를 해주지 않으면 시간초과
        # if문을 통해 이전 재귀에서 탐색한 범위를 제외하고 for문을 수행하도록
        for i in range(x, n):
            if i == x: k = y
            else: k = 0
            for j in range(k, m):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    build_walls(cnt_walls + 1, i, j + 1)
                    arr[i][j] = 0


build_walls(0, 0, 0)
# 안전영역의 크기는 전체크기 - 바이러스의 최소값 - 벽의개수
print(m * n - minV - cntW - 3)
