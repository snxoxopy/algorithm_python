"""
---
title:  "[Python] PRGRMS_120814_피자_나눠_먹기_1"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/120814"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
  - math
tags:
  - PROGRAMMERS
  - stack
---

문제 이해: 5분
구현: 5분
Debug: 분
참고 자료:
"""

def solution(n):
    answer = 0
    n_pizza = 7
    for i in range(1, 101):
        if n_pizza * i >= n:
            answer = i
            break
    return answer