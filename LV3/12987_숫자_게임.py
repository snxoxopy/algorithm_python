
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

from collections import deque


def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    qA = deque(A)
    qB = deque(B)
    if min(A) < max(B):
        while qB:
            numB = qB.popleft()
            for numA in qA:
                if numB > numA:
                    answer += 1
                    qA.popleft()
                    break
    else:
        for i in range(len(A)):
            if B[i] > A[i]:
                answer += 1

    return answer