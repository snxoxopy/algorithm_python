# https://www.acmicpc.net/problem/11866
# 문제이해: 6분
# 구현: 20분
# Debug: 15분

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())
queue = deque()
for i in range(1, n + 1): queue.append(i)

answer = "<"
for j in range(0, n):
    queue.rotate((k - 1) * -1)
    answer += str(queue.popleft()) + ", "

answer = answer[:-2] + ">"
print(answer)