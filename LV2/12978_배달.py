
"""
---
title:  "[Python] PRGRMS_12978_배달"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/12978"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - PROGRAMMERS
  - Dijkstra's
---

문제 이해: 분
구현: 분
Debug: 분
참고 자료: 문제 질문 하기
https://m.blog.naver.com/kks227/220796029558
"""

import heapq


def dijkstra(r, n):
    q = []
    heapq.heappush(q, [1, 0])
    # N = 마을 개수
    # road = [nd1, nd2, cost]
    # K = 배달 가능 시간
    dist = [float('inf') for _ in range(n + 1)]
    dist[1] = 0

    while q:
        # 현재 nd와 비용
        cur_nd, cur_cst = heapq.heappop(q)
        for src, dst, cst in r:
            n_cst = cst + cur_cst
            # src = 현재 선택된 nd && 목적지까지 낮은 비용
            if src == cur_nd and n_cst < dist[dst]:
                dist[dst] = n_cst  # 최소 비용 갱신
                heapq.heappush(q, [dst, n_cst])
            # dst = 현재 선택된 nd && 출발지까지 낮은 비용
            elif dst == cur_nd and n_cst < dist[src]:
                dist[src] = n_cst
    return dist


def solution(Node, road, K):
    # 마을의 개수
    answer = dijkstra(road, Node)

    return len([x for x in answer if x <= K])