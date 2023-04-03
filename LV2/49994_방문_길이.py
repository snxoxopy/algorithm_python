"""
---
title:  "[Python] PRGRMS_49994_방문_길이"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/49994"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - PROGRAMMERS
  - implementation
---

문제 이해: 5분
구현: 45분
Debug: 분
참고 자료:

"""

def solution(dirs):
    # 방문 길이
    answer = 0
    rt = set()
    go = dict(U = 0, D = 1, R = 2, L = 3)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    r, c = 0, 0

    for d in dirs:
        nr, nc = r + dr[go[d]], c + dc[go[d]]
        if -6 < nr < 6 and -6 < nc < 6:
            if not (r, c, nr, nc) in rt:
                rt.add((r, c, nr, nc))
                rt.add((nr, nc, r, c))
                answer += 1
            r, c = nr, nc

    return answer