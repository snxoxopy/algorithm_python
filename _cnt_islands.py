"""
https://www.acmicpc.net/problem/4963
# Date: 03-18-21
# Input data and DFS
"""
import sys
from collections import deque

sys.setrecursionlimit(10000)


def _cnt_islands(x, y, graph):
    if x <= -1 or x >= len(graph) or y <= -1 or y >= len(graph[0]):
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        _cnt_islands(x - 1, y, graph)
        _cnt_islands(x, y - 1, graph)
        _cnt_islands(x + 1, y, graph)
        _cnt_islands(x, y + 1, graph)
        _cnt_islands(x - 1, y - 1, graph)
        _cnt_islands(x + 1, y + 1, graph)
        _cnt_islands(x - 1, y + 1, graph)
        _cnt_islands(x + 1, y - 1, graph)
        return True
    return False


# main
l_map = []
ans = deque()
c, r = 1, 1
while c + r != 0:
    res = 0
    c, r = map(int, input().split())

    for i in range(r): l_map.append(list(map(int, input().split())))
    for i in range(r):
        for j in range(c):
            if _cnt_islands(i, j, l_map) is True: res += 1
    ans.append(res)
    l_map = []
while ans:
    print(ans.popleft())

"""
def _cnt_islands(x, y):
    if x <= -1 or x >= r or y <= -1 or y >= c or l_map[x][y] != 1:
        return

    l_map[x][y] = 0

    _cnt_islands(x - 1, y)
    _cnt_islands(x, y - 1)
    _cnt_islands(x + 1, y)
    _cnt_islands(x, y + 1)
    _cnt_islands(x - 1, y - 1)
    _cnt_islands(x + 1, y + 1)
    _cnt_islands(x - 1, y + 1)
    _cnt_islands(x + 1, y - 1)


res = 0
for i in range(r):
    for j in range(c):
        if l_map[i][j] == 1:
            _cnt_islands(i, j)
            res += 1
"""
