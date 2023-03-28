"""
---
title:  "[Python] PRGRMS_42628_이중우선순위큐"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/42628"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - PROGRAMMERS
  - heap
---

문제이해: 5분
구현: 35분
Debug: 15분
참고자료
"""

import heapq


def solution(operations):
    answer = [0, 0]
    arr = []
    q = []
    for strr in operations:
        arr.append(strr.split())

    for oprt, oprnd in arr:
        num = int(oprnd)
        if oprt == 'I':
            q.append(num)
            heapq.heapify(q)
        else:
            # print(num)
            if len(q) == 0:
                continue
            else:
                if num == -1:  # 최소값 삭제
                    heapq.heappop(q)
                elif num == 1:  # 최대값 삭제
                    for i in range(len(q)):
                        q[i] *= -1
                    heapq.heapify(q)
                    heapq.heappop(q)
                    for i in range(len(q)):
                        q[i] *= -1
                    heapq.heapify(q)

    if len(q) > 0:
        answer = [max(q), min(q)]
    else:
        answer = [0, 0]

    return answer