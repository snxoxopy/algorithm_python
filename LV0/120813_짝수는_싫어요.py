"""
---
title:  "[Python] PRGRMS_120813_짝수는_싫어요"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/120813"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
  - math
tags:
  - PROGRAMMERS
---

문제 이해: 5분
구현: 12분
Debug: 분
참고 자료
"""

# O(N) List Comprehension
def solution(n):
    return [x for x in range(1, n+1) if x % 2 == 1]


# O(N)
def solution(n):
    answer = []
    for num in range(1, n+1):
        if (num % 2) == 1:
            answer.append(num)
    return answer