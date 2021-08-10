
"""
---
title:  "[Python] BOJ_1260_DFS와BFS"
excerpt: "https://www.acmicpc.net/problem/1260"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - DFS
  - BFS
---

문제이해: 분
구현: 분
Debug: 분
참고자료

"""

import sys
from collections import deque

sys.stdin = open("dfs/input.txt","r")

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
n, m, v = map(int, sys.stdin.readline().rstrip().split())
#print(n, m, v)

# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
# 인접 리스트 표현
graph = [[] for _ in range(n+1)]
graph[0] = [0,0]
for _ in range(m):
    node1, node2 = map(int,sys.stdin.readline().rstrip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    graph[node1].sort()
    graph[node2].sort()

#print(graph)

# DFS
# 재귀함수, 종료조건: 모든 node 방문 시
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]: dfs(graph, i, visited)

visited = [False for _ in range(n+1)]
dfs(graph, v, visited)