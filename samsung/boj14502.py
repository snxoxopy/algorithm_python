"""
---
title:  "[Python] BOJ_14502_연구소"
excerpt: "https://www.acmicpc.net/problem/14502"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - BFS
---

문제이해: 7분
구현: 20분
Debug: 40분
참고자료
https://www.acmicpc.net/source/25345356
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")


# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며,
# 직사각형은 1×1 크기의 정사각형으로 나누어져 있다.
# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

# 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
n, m = map(int, sys.stdin.readline().split())
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다.
# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다.
# 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
# 빈 칸의 개수는 3개 이상이다.
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#print(arr)

arr, lst_virus, lst_blks, n_walls = [], [], [], 0
# 완전 탐색
# 벽을 세울수 있는 모든 좌표를 찾는다.
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if arr[i][j] == 0: lst_blks.append((i, j))
        elif arr[i][j] == 1: n_walls += 1
        else: lst_virus.append((i, j))

# 세운 벽위치에서 안전 영역의 크기를 구한다.
dr, dc = (-1, 0, 1, 0), (0, -1, 0, 1)

def bfs(i, j, visited, cnt):
    q = deque([[i, j]])
    cnt = 1
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if -1 < nr < n and -1 < nc < m and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                # 벽이 아닌 곳
                visited[nr][nc] = 1
                cnt += 1
                q.append([nr, nc]) # 안전영역
    return cnt


def recur(start, end, num):
    if num == 0: # 3개 벽 세우는 조합이 끝나면
        visited = [[0] * m for _ in range(n)]
        #cnt = 0
        for i, j in lst_virus:
            if visited[i][j] == 0: # 미 방문 상태면
                visited[i][j] = 1
                cnt = bfs(i, j, visited)
        return n * m - cnt - n_walls - 3

    res = 0
    # 벽 조합 찾기
    for i in range(start, end):
        zr, zc = lst_blks[i]
        arr[zr][zc] = 1 # 벽 세우기
        res = max(res, recur(i + 1, end, num - 1))
        arr[zr][zc] = 0 # 벽 없애기
    #print(res)
    return res


# 안전 영역 크기 최대 값을 업데이트한다.

# ======================== main
print(recur(0, len(lst_blks), 3))
