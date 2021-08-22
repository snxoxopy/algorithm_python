"""
---
title:  "[Python] BOJ_7569_토마토"
excerpt: "https://www.acmicpc.net/problem/7569"
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
구현: 33분
Debug: 12분
참고자료
https://ca.ramel.be/80
"""

import sys
from collections import deque

sys.stdin = open("bfs/input.txt","r")

m, n, h = map(int, sys.stdin.readline().split())
print(m, n, h)

q = deque()
arr = []

for k in range(h):
    tmp = []
    for i in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for j in range(m):
            if tmp[i][j] == 1: q.append([k,i,j])
    arr.append(tmp)

print(arr)

dr, dc, dh = (0, -1, 0, 1, 0, 0), (-1, 0, 1, 0, 0, 0), (0, 0, 0, 0, -1, 1)


def bfs():
    while q:
        z, r, c = q.popleft()
        for d in range(len(dr)):
            nz, nr, nc = z + dh[d], r + dr[d], c + dc[d]
            if -1 < nz < h and -1 < nr < n and -1 < nc < m and arr[nz][nr][nc] == 0:
                arr[nz][nr][nc] = arr[z][r][c] + 1
                q.append([nz, nr, nc])

bfs()
result = 0
flag = False

for i in arr:
    for j in i:
        if 0 in j: flag = True
        result = max(result, max(j))

print(-1) if flag else print(result-1)
