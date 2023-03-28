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
https://school.programmers.co.kr/learn/courses/30/lessons/42628/solution_groups?language=python3
"""

import heapq

def solution(operations):
    arr = []
    q = []
    for strr in operations:
        arr.append(strr.split())

    for oprt, oprnd in arr:
        num = int(oprnd)
        if oprt == 'I':
            heapq.heappush(q, num)
        elif len(q) > 0:
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

"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
"""