"""
---
title:  "[Python] BOJ_2667_단지번호붙이기"
excerpt: "https://www.acmicpc.net/problem/2667"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - DFS
---

문제이해: 10분
구현: 70분
Debug: 분
참고 자료
"""

import sys
sys.stdin = open("input.txt","r")
import timeit

# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

#print(graph)

# 첫 번째 줄에는 총 단지수를 출력하시오.
# 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

# 연결된 graph 완전 탐색
# 연결 되었다는 것은
# 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(fr, fc):
    global cnt_one

    if not (-1 < fr < n and -1 < fc < n): return False

    if graph[fr][fc] == 1:
        graph[fr][fc] = 0
        cnt_one += 1
        for d in range(4):
            nr, nc = fr + dr[d], fc + dc[d]
            dfs(nr, nc)
        return True
    return False

t_start = timeit.default_timer()
cnt_group, cnt_one = 0, 0
lst_cnt = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt_group += 1
            lst_cnt.append(cnt_one)
            cnt_one = 0



print(cnt_group)
lst_cnt = sorted(lst_cnt)
for _ in range(len(lst_cnt)): print(lst_cnt.pop(0))
t_end = timeit.default_timer()

print("t = %f[ms]"%((t_end-t_start)*1000))