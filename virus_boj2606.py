"""
---
title:  "[Python] BOJ_2606_바이러스"
excerpt: "https://www.acmicpc.net/problem/2606"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - BFS
---

문제이해: 5분
구현: 30분
Debug: 4분
참고자료
- https://yurimkoo.github.io/algorithm/2020/05/09/time-complexity-1.html
- https://mimimimamimimo.tistory.com/2
- https://soobarkbar.tistory.com/61
"""

import sys
from collections import deque
import timeit

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())
#print(n)

t_start = timeit.default_timer()
graph =[[] for _ in range(n+1)]
graph[0] = [0, 0]
visited = [False for _ in range(n+1)]


for _ in range(int(sys.stdin.readline().rstrip())):
    node1, node2 = map(int, sys.stdin.readline().rstrip().split())
    #print(node1, node2)
    graph[node1].append(node2)
    graph[node2].append(node1)

def bfs(graph, start, visited):
    visited[start] = True
    q = deque([start])
    cnt = 0
    while q:
        node = q.popleft()
        #print(node, end=" ")
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                cnt += 1
                visited[i] = True

    return print(cnt)

bfs(graph, 1, visited)
t_end = timeit.default_timer()
print("소요시간 %f[ms]"%((t_end - t_start)*1000))