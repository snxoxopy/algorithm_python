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
def solution(n, works):
    answer = 0
    # 피로도 += 남은일 작업량^2 -> (시작한 시점 - 지금까지 한 일)^2
    # 야근 피로도 최소
    # N시간
    # 남은일 작업량 works = []
    # 최고 집합
    works.sort()
    hour = n

    if n > sum(works):
        return 0
    else:
        while hour != 0:
            for i in range(len(works) - 1, -1, -1):
                works[i] -= 1
                hour -= 1
                if hour == 0: break
            # else: works[i] -= 1

            # print(works)

        for task in works:
            answer += (task) ** 2

    return answer