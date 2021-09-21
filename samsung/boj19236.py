"""
---
title:  "[Python] BOJ_19236_청소년 상어"
excerpt: "https://www.acmicpc.net/problem/19236"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - Implementation
  - BFS
---

문제이해: 분
구현: 분
Debug: 분
참고자료
https://junboom.tistory.com/20
https://www.acmicpc.net/source/28633747
https://www.acmicpc.net/source/26936113
"""
import sys
from collections import deque
import copy
sys.stdin = open("input.txt", "r")


# 4×4크기의 공간이 있고, 크기가 1×1인 정사각형 칸으로 나누어져 있다.
# 각 물고기는 번호와 방향을 가지고 있다.
# 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며,
# 두 물고기가 같은 번호를 갖는 경우는 없다.


#arr = [[[]]*4 for _ in range(4)]
arr = [[None] * 4 for _ in range(4)]
#tmp = []

for i in range(4):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        #arr[i][j] = [tmp[2 * j] - 1, tmp[2 * j + 1] - 1] # idx[0,7], dir[0,15]
        arr[i][j] = [tmp[2 * j] - 1, tmp[2 * j + 1] - 1]

#print(arr)

# 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dr, dc = (-1, -1, 0, 1, 1, 1, 0, -1), (0, -1, -1, -1, 0, 1, 1, 1)


def find_fishes(idx, arr):
    # 물고기가 존재하지 않으면 빈칸 or 상어 자리일 것이다.
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == idx:
                return i, j, arr[i][j][1]
    return 0, 0, -1


def fishes_move(arr):
    # 물고기는 번호가 작은 물고기부터 순서대로 이동한다.
    for i in range(16):
        r, c, d = find_fishes(i, arr)
        if d != -1:
            # 빈칸이거나 상어자리인 경우를 제외하고
            # 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
            for i in range(8):
                nr, nc = r + dr[(d + i) % 8], c + dc[(d + i) % 8]
                # 물고기 이동 가능: 빈칸, 다른 물고기 있는칸
                # 물고기 이동 불가능: 상어, 범위 밖
                if -1 < nr < 4 and -1 < nc < 4 and arr[nr][nc][0] != -1: #상어 아님 -> 빈칸 혹은 다른 물고기 자리
                    # 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.
                    arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
                    arr[nr][nc][1] = (d + i) % 8
                    break
    #print(arr)
    #return arr


# 상어가 이동할 수 있는 위치와, 상어가 먹을 수 있는 물고기 번호의 합 최대 값을 출력
# 상어 위치 = -1, 빈칸 = -2
def bfs(arr):
    max_fishes = 0
    cnt = arr[0][0][0] + 1 # 1_fish
    arr[0][0][0] = -1 # 물고기 방문 처리 (상어 자리)
    q = deque([[arr, 0, 0, cnt]])

    # 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다.
    # 업데이트 되는 좌표를 기준으로 이동할 수 없는 칸이 존재할 때 까지 BFS
    while q:
        narr, r, c, ncnt = q.popleft()
        d = narr[r][c][1]

        # 물고기 먹은 최대 수 업데이트
        max_fishes = max(ncnt, max_fishes)

        # 물고기 이동
        fishes_move(narr)

        # 물고기의 이동이 모두 끝나면 상어가 이동한다.
        # 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다.
        # 상어 자리 = -1, 빈칸 = -2
        for i in range(1, 5):
            nr, nc = r + dr[d] * i, c + dc[d] * i
            if -1 < nr < 4 and -1 < nc < 4 and narr[nr][nc][0] != -2:
                cp_arr = copy.deepcopy(narr)
                cp_arr[r][c] = [-2, -1] # idx 빈칸, d 빈칸
                n_fish = cp_arr[nr][nc][0] + 1
                cp_arr[nr][nc] = [-1, cp_arr[nr][nc][1]] # 상어 방문 표시
                q.append([cp_arr, nr, nc, ncnt + n_fish])

    return max_fishes

# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.
print(bfs(arr))
