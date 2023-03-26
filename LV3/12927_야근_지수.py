"""
---
title:  "[Python] PRGRMS_12927_야근_지수"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/12927"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - PROGRAMMERS
  - heap
---

문제 이해: 5분
구현: 60분
Debug: 60분
참고 자료:

"""
import heapq


def solution(n, works):
    answer = 0
    if sum(works) < n:
        return answer

    for i in range(len(works)):
        works[i] *= -1

    heapq.heapify(works)

    for i in range(n):
        # 작은 값 부터 반환
        m = heapq.heappop(works)
        # -1 보다 클 경우 이미 끝난 일
        if m > -1:
            heapq.heappush(works, m)
        # 1시간동안 작업량 1처리
        m += 1  # 음수처리했으므로 +1
        heapq.heappush(works, m)

    for _ in range(len(works)):
        task = heapq.heappop(works)
        # 음수를 곱하면 양수가 되므로 추가처리 불필요
        answer += task ** 2

    return answer