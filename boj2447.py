"""
---
title:  "[Python] BOJ_2447_별찍기-10"
excerpt: "https://www.acmicpc.net/problem/2447"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - recursion
---

문제이해: 분
구현: 분
Debug: 분
참고자료
https://study-all-night.tistory.com/5
"""


def draw_star(n):
    global Map

    if n == 3:
        Map[0][:3] = Map[2][:3] = [1] * 3
        Map[1][:3] = [1, 0, 1]
        return

    a = n // 3
    draw_star(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]  # 핵심 아이디어


N = int(input())

# 메인 데이터 선언
Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()