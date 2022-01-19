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

문제 이해: 분
구현: 분
Debug: 분
참고 자료
https://study-all-night.tistory.com/5
"""


def draw_star(n):
    global arr

    # 종료 조건
    # 3x3 단위 배열 초기 값 생성
    if n == 3:
        arr[0][:3] = arr[2][:3] = [1] * 3
        arr[1][:3] = [1, 0, 1]
        return

    # 현 단계의 규칙 배열 크기 값을 반환
    # N = 27 -> 9 -> 3
    # a =  9 -> 3 -> 1
    a = n // 3

    # 재귀 함수 호출
    draw_star(n // 3)

    # 도장 찍기
    # 1) 단위 배열 크기 반복
    for i in range(3):
        for j in range(3):
            # 규칙 배열 중 가운데 배열을 초기 값으로 유지하기 위함
            if i == 1 and j == 1: continue
            # n = 3^i 일때는 가운데를 비워두고 "n = 3^(i-1) 일때의 별 배열" ; i > 1
            # 2) 규칙 배열 크기 반복
            for k in range(a):
                arr[a * i + k][a * j:a * (j + 1)] = arr[k][:a]

# input
N = int(input())

# system

# arr 초기화
arr = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

# output
# 별 찍기: 1 = * / 0 = ' '
for i in arr:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()