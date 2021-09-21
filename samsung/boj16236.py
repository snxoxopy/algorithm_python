"""
---
title:  "[Python] BOJ_16236_마법사 상어와 파이어스톰"
excerpt: "https://www.acmicpc.net/problem/16236"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - Implementation
---

문제이해: 분
구현: 분
Debug: 분
참고자료
"""

import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#print(n, arr)

# 상어 위치 찾기
#sr, sc = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9: sr, sc = i, j
arr[sr][sc] = 0 # 방문 처리, 반례 5

# =============================================================== 최단 거리
# 현재 상어 좌표에서 상어가 지나갈 수 있는 거리를 계산한다.
# 상, 하, 좌, 우
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(sr, sc, arr, len_shark):
    q = deque([[sr, sc]])
    dist = [[-1] * n for _ in range(n)]
    dist[sr][sc] = 0  # 방문처리

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if -1 < nr < n and -1 < nc < n:
                # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
                if dist[nr][nc] == -1 and arr[nr][nc] <= len_shark:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append([nr, nc])

    return dist

# =============================================================== main

len_shark, n_fishes, ans = 2, 0, 0

while True:
    min_dist = 1e9
    dist = bfs(sr, sc, arr, len_shark)
    # 완전 탐색
    for i in range(n):
        for j in range(n):
            # 먹을 수 있는 경우
            #if dist[i][j] != -1 and 0 < arr[i][j] < len_shark:
            if -1 < dist[i][j] < min_dist and 0 < arr[i][j] < len_shark:
                #if dist[i][j] < min_dist:
                min_dist = dist[i][j]
                sr, sc = i, j
                #arr[sr][sc] = 0

    if min_dist == 1e9:
        print(ans)
        break
    else:
        #sr, sc = r, c
        ans += min_dist
        arr[sr][sc] = 0  # 물고기 먹은 표시
        n_fishes += 1
        if len_shark == n_fishes:
            len_shark += 1
            n_fishes = 0