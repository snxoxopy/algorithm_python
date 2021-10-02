"""
---
title:  "[Python] BOJ_19238_스타트택시"
excerpt: "https://www.acmicpc.net/problem/19238"
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
문제이해: 10분
구현: 분
Debug: 분
https://www.acmicpc.net/board/view/63883
"""

import sys
from collections import deque
sys.stdin = open("input.txt", "r")


n, m, fuel = map(int, sys.stdin.readline().split())
# print(n, m)

#  0은 빈칸, 1은 벽을 나타낸다.
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print('arr = ', arr)

# 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다. 행
tr, tc = map(int, sys.stdin.readline().split())
# print("ir, ic=", ir, ic)

# M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다.
info_dep = {}
for cstm in range(m):
    info_dep[cstm] = list(map(int, sys.stdin.readline().split()))

# print(info_dep)
# info_dep[m] = [] # 출발지rc, 목적지rc
# print(info_dep[0])

dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]

def bfs(ir, ic):
    visited = [[0] * n for _ in range(n)]
    visited[ir-1][ic-1] = 1
    q = deque([[ir-1, ic-1, 0]])
    while q:
        r, c, dist = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if -1 < nr < n and -1 < nc < n and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                q.append([nr, nc, dist+1])

                visited[nr][nc] = visited[r][c] + 1
    return visited

def find_closest_cust(arr_dist):
    dist = []
    # print('info_dep = ',info_dep)
    for cust in info_dep.keys():
        dr, dc, ar, ac = info_dep[cust]
        dist.append([cust, [arr_dist[dr - 1][dc - 1] - 1, dr, dc, ar, ac]]) # 출발지
        # idx += 1

    # 오름차순 정렬
    # print(dist)
    # dict_dist = list(dist.values())
    dict_dist = sorted(dist, key=lambda x: [x[1], x[0]])
    # print('dict_dist=', dict_dist)

    return dict_dist

# 이동하기
cnt_cust = 0
for _ in range(m):

    # 현재 택시 좌표에서 최단거리 승객 고르기 -> BFS
    arr_dist = bfs(tr, tc)
    # print('arr_dist', arr_dist)

    # 여러 승객이 있다면, 행 번호 작은 순서
    sort_cust = find_closest_cust(arr_dist)

    # print('sort_cust[0],', sort_cust[0])
    idx, info = sort_cust[0]
    # print('idx', idx)
    #   한칸 이동시 연료 = 연료 - 1
    consum, der, dec, ar, ac = info[0], info[1], info[2], info[3], info[4]
    # print('consum', consum)

    fuel -= consum
    #   연료 바닥 -> 이동 실패 -> 업무 종료
    if fuel < 1 or consum < 0 and (cnt_cust < m):
        fuel = -1
        break

    # 승객 위치 도착
    tr, tc = der, dec
    arr_dist = bfs(tr, tc)
    consum = (arr_dist[ar - 1][ac - 1] - 1)
    fuel -= (arr_dist[ar - 1][ac - 1] - 1)

    if fuel < 0 or consum < 0 and (cnt_cust < m):
        fuel = -1
        break
    # 연료 += 소모연료 * 2
    fuel += consum * 2

    # 목적지도착
    tr, tc = ar, ac

    # 승객 내리기
    del info_dep[idx]
    cnt_cust += 1

print(fuel)