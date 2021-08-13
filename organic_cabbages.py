"""
---
title:  "[Python] BOJ_1012_유기농_배추"
excerpt: "https://www.acmicpc.net/1012/"
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
구현: 51분
Debug: 분
참고자료
https://deep-learning-study.tistory.com/615
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")

t = int(sys.stdin.readline().rstrip())

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


# 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어,
# 그 배추들 역시 해충으로부터 보호받을 수 있다.

# 흰 지렁이 = 배추 보호
# 최소 배추흰지렁이 마리 수 = 배추가 있는 구역


def bfs(graph, fr, fc):
    global cnt

    graph[fr][fc] = 0
    q = deque([[fr, fc]])

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if -1 < nr < m and -1 < nc < n and graph[nr][nc] == 1:
                q.append([nr, nc])
                graph[nr][nc] = 0
    cnt += 1



for _ in range(t):
    # 가로, 세로, 위치개수
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    arr = [[0 for _ in range(n)] for _ in range(m)]
    # r, c
    #lst_pos = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(k)]
    for _ in range(k):
        r, c = map(int, sys.stdin.readline().rstrip().split())
        arr[r][c] = 1
    #print(arr)

    q = deque([0, 0])
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1: bfs(arr, i, j)
    print(cnt)