"""
---
title:  "[Python] BOJ_2178_미로탐색"
excerpt: "https://www.acmicpc.net/problem/2178"
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
구현: 24분
Debug: 분
참고자료
https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-2178%EB%B2%88-%EB%AF%B8%EB%A1%9C-%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
"""
import sys
from collections import deque

# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
# 각각의 수들은 붙어서 입력으로 주어진다.

# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 
# 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
sys.stdin = open("bfs/input.txt","r")
n, m = map(int, sys.stdin.readline().split())

#print(n, m)

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
#print(graph)

# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
q = deque([[0, 0]])

while q:
    r, c = q.popleft()
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if -1 < nr < n and -1 < nc < m and graph[nr][nc] == 1:
            q.append([nr, nc])
            graph[nr][nc] = graph[r][c] + 1

print(graph[n-1][m-1])

