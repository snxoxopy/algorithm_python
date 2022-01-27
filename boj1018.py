"""
---
title:  "[Python] BOJ_1018_체스판_다시_칠하기"
excerpt: "https://www.acmicpc.net/problem/1018"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - Brute-force search
---

문제 이해: 18분
구현: 분
Debug: 분
참고 자료
https://god-gil.tistory.com/62
"""
import sys
sys.stdin = open("input.txt")

n, m = map(int, sys.stdin.readline().split())
# print(n, m)

arr = [list(map(str, sys.stdin.readline())) for _ in range(n)]
# print(arr)
# print(arr[0][1])
min_value = list()

for i in range(n - 7):      # 전체 행 탐색
    for j in range(m - 7):  # 전체 열 탐색
        wi, bi = 0, 0       # 2가지 경우의 수 배열 값 초기화
        for k in range(i, i + 8):       # 8개 행 탐색
            for l in range(j, j + 8):   # 8개 열 탐색
                if (k + l) % 2 == 0:    # [경우 1) W / 경우 2) B] 가 있어야 할 위치
                    if arr[k][l] != 'W': wi += 1
                    else: bi += 1
                else:                   # [경우 1) B / 경우 2) W] 가 있어야 할 위치
                    if arr[k][l] != 'B': wi += 1
                    else: bi += 1
        min_value.append(wi)
        min_value.append(bi)
        #print(min_value)    # 바꿀 필요가 없다면, wi or bi 값이 증가하지 않으므로 0을 반환한다.

print(min(min_value))