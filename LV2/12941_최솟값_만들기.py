
"""
---
title:  "[Python] PRGRMS_12941_최솟값_만들기"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/12941"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
  - math
tags:
  - PROGRAMMERS
  - math
---

문제 이해: 5분
구현: 20분
Debug: 12분
참고 자료: 문제 질문하기

"""

def solution(A,B):
    answer = 0
    # 최소(A) * 최대(B) 결과의 누적 합은 최소값이다.
    # 증명
    # A = [a, b, c], B = [d, e, f]; a <= b <= c, d <= e <= f
    # Q >= R 증명
    # Q     = a * d + b * e + c * f
    # R     = a * f + b * e + c * d
    # Q - R = a(d-f) + b(e-e) + c(f-d)
    # Q - R = a(d-f) + c(f-d) >= 0
    # Q - R = (f-d)(c-a) >= 0
    # because of (f >= d) and (c >= a)

    A.sort()
    B.sort()
    # print(A, B)
    e_sum, e_mul = 0, 0
    for i in range(len(A)):
        e_mul = A[i] * B[len(B) - i - 1]
        answer += e_mul

    return answer