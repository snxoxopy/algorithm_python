"""
https://www.acmicpc.net/problem/2606
# Date: 03-18-21
# Input data and BFS
"""
from collections import deque


def virus(net, start, visited):
    ans = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        ans += 1
        for i in net[v]:
            if visited[i] is False:
                queue.append(i)
                visited[i] = True
    return ans - 1


n_com = int(input())
n_oth = int(input())
visited = [False] * (n_com + 1)
graph = [[] for _ in range(n_com + 1)]

for _ in range(1, n_oth + 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(virus(graph, 1, visited))
