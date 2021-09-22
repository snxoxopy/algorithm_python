"""
---
title:  "[Python] BOJ_3190_뱀"
excerpt: "https://www.acmicpc.net/problem/3190"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - Implementation
  - queue
---

문제이해: 13분
구현: 분
Debug: 분
참고자료
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")


# 첫째 줄에 보드의 크기 N이 주어진다.
n = int(input())
k = int(input())

# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
arr = [[0]* n for _ in range(n)]

for _ in range(k):
    i, j = map(int, sys.stdin.readline().split())
    arr[i - 1][j - 1] = 1 # 사과
# print(arr)

# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
l = int(input())

# 정수 X와 문자 C로 이루어져 있으며.
cmd = dict()
for _ in range(l):
    x, c = map(str, sys.stdin.readline().split())
    cmd[int(x)] = c

#print(cmd)

# ====================================== main
# 게임은 NxN 정사각 보드위에서 진행되고
# 몇몇 칸에는 사과가 놓여져 있다.
# 게임이 시작할때 뱀은 맨위 맨좌측(1,1)에 위치하고
# 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.


# 우 하 좌 상
dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
r, c, d = 0, 0, 0 # 초기 뱀 상태
t = 1 # 뱀이 맨위 맨좌측 위치한 순간부터 시작
arr[r][c] = 2

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

# 사과를 먹으면 뱀 길이가 늘어난다.
# 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.


# queue를 어떻게 사용 할까?
# First in First out, 가장 먼저 지나간 자리 순서대로 뱀의 몸을 넣는다.
# 사과 O > 꼬리 유지 append, 사과 X > 꼬리 제거 pop
# arr = 1 사과, arr = 2 뱀, arr = 0 빈칸
q = deque([[r, c]])

while True:
    r, c = r + dr[d], c + dc[d]
    if -1 < r < n and -1 < c < n and arr[r][c] != 2: # 벽 안
        if arr[r][c] != 1:
            sr, sc = q.popleft()
            arr[sr][sc] = 0 # 꼬리 제거
        q.append([r, c])
        arr[r][c] = 2

        # 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
        if t in cmd.keys():
            rotate = cmd[t]
            # L: 우 상 좌 하 0>3>2>1>0
            # D: 우 하 좌 상 0>1>2>3>0
            if rotate == "L": d = (d - 1) % 4
            else: d = (d + 1) % 4
        t += 1
    else: print(t); break # 벽 밖이거나, 뱀 자기 자신일 때