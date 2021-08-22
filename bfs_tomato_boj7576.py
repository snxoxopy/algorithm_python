"""
---
title:  "[Python] BOJ_7576_토마토"
excerpt: "https://www.acmicpc.net/problem/7576"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - BFS
---

문제이해: 10분
구현: 36분
Debug: 1분
참고자료
https://wookcode.tistory.com/32
"""
import sys
from collections import deque
sys.stdin = open("bfs/input.txt", "r")
n, m = map(int, sys.stdin.readline().split())
dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
q = deque()
arr = []
for i in range(m):
    arr.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if arr[i][j] == 1: q.append([i, j])

while q:
    r, c = q.popleft()
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if -1 < nr < m and -1 < nc < n and arr[nr][nc] == 0:
            arr[nr][nc] = arr[r][c] + 1
            q.append([nr, nc])
            
check, max_days = True, 0

for i in arr:
    max_days = max(max(i), max_days)

for i in arr:
    if 0 in i:
        check = False
        print(-1)
        break

if check: print(max_days-1)