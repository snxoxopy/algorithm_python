"""
---
title:  "[Python] BOJ_11729_하노이의 탑 이동 순서"
excerpt: "https://www.acmicpc.net/problem/11729"
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
https://study-all-night.tistory.com/6
"""


def recur(n, start, end):
    # 종료 조건
    if n == 1:
        print(start, end)
        return
    #1 S -> ? 이동
    recur(n - 1, start, 6 - start - end)
    # 2 S -> E 이동
    print(start, end)
    # 3 ? -> E 이동
    recur(n - 1, 6 - start - end, end)

n = int(input())
# 전체 경우의 수 - n개의 원판이 전부 이동 안한 경우
print(2 ** n - 1)

recur(n, 1, 3)
