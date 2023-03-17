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

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.3MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
"""

def solution(n):
    return (n - 1) // 7 + 1