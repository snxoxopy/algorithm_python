# 예제 입력 4의 경우 2393개의 좌표가 존재한다.
# 위 경우의 좌표 조합을 계산할 경우 2394_C_4 번의 연산이 필요하므로 비효율적이다.

import sys
from copy import deepcopy
from collections import deque
sys.stdin = open('input.txt', 'r')
# input
n = int(input())
# arr = [c, r, d, g]
# r c는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다.
arr = [list(map(int, input().split())) for _ in range(n)]
# 0: c좌표가 증가하는 방향 (→)
# 1: r좌표가 감소하는 방향 (↑)
# 2: c좌표가 감소하는 방향 (←)
# 3: r좌표가 증가하는 방향 (↓)
# dir = ((0, 1), (-1, 0), (0, -1), (1, 0))
dr = (0, -1, 0, 1)
dc = (1, 0, -1, 0)


pos_rect = []

# system

results = []
picked = deque()
num_rect = 0



def cnt_rect(picked_comb):
    global num_rect
    row_max = max(picked_comb[0][0], picked_comb[1][0], picked_comb[2][0], picked_comb[3][0])
    row_min = min(picked_comb[0][0], picked_comb[1][0], picked_comb[2][0], picked_comb[3][0])
    col_max = max(picked_comb[0][1], picked_comb[1][1], picked_comb[2][1], picked_comb[3][1])
    col_min = min(picked_comb[0][1], picked_comb[1][1], picked_comb[2][1], picked_comb[3][1])
    if row_max - row_min == 1 and col_max - col_min == 1:
        if picked_comb[0][0] == picked_comb[1][0] ^ picked_comb[2][0] ^ picked_comb[3][0]:
            if picked_comb[0][1] == picked_comb[1][1] ^ picked_comb[2][1] ^ picked_comb[3][1]:
                #print(picked_comb[0][0], picked_comb[1][0], picked_comb[2][0], picked_comb[3][0])
                #print(picked_comb[0][1], picked_comb[1][1], picked_comb[2][1], picked_comb[3][1])
                num_rect += 1

def comb_pos(pos):
    deep_pos = deepcopy(pos)
    if len(picked) == 4:
        cnt_rect(picked)
        return
    else:
        for [i, j] in pos:
            picked.append([i, j])
            deep_pos.remove([i, j])
            comb_pos(deep_pos)
            picked.pop()


# main
rotate = deque()
for i in range(n):
    c, r, d, g = arr[i]
    pos_rect.append([r, c])
    rotate.append(d)
    for _ in range(g):
        reverse = list(reversed(rotate))
        for j in reverse:
            if j + 1 == 4: rotate.append(0)
            else: rotate.append(j + 1)

    while rotate:
        cw = rotate.popleft()
        nr, nc = r + dr[cw], c + dc[cw]
        if -1 < nr < 101 and -1 < nc < 101:
            pos_rect.append([nr, nc])
            r, c = nr, nc

set_pos = deque()
for v, w in pos_rect:
    if [v, w] not in set_pos:
        set_pos.append([v, w])
print(set_pos)
print(len(set_pos))

# output
# 첫째 줄에 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력한다.
# 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수
comb_pos(set_pos)
print(num_rect)
