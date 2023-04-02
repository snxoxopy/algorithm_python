
"""
---
title:  "[Python] PRGRMS_12987_숫자게임"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/12987"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - PROGRAMMERS
  - sort
---

문제 이해: 10분
구현: 100분
Debug: 분
참고 자료:
"""

def solution(A, B):
    answer, j = 0, 0
    A = sorted(A)
    B = sorted(B)

    for i in range(len(B)):
        if B[i] > A[j]:
            answer += 1
            j += 1

    return answer