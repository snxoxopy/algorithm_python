"""
---
title:  "[Python] PRGRMS_12909_올바른_괄호"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/12909"
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
구현: 20분
Debug: 10분
참고 자료:
"""

def solution(s):
    st = []
    for p in s:
        if p == '(':
            st.append(p)
        elif p == ')' and len(st) == 0:
            return False
        else: # p == ')' and len(st) > 0:
            st.pop()
    if len(st) == 0: return True
    else: return False