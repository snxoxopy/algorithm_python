# https://www.acmicpc.net/problem/2164
# 문제이해: 2분
# 구현: 10분
# Debug: -

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n = int(input())
queue = deque()

for i in range(1, n+1): queue.append(i)
while queue:
    print(queue.popleft()) if len(queue) == 1 else queue.popleft()
    queue.rotate(-1)