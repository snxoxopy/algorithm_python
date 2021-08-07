# https://www.acmicpc.net/problem/1966
# 문제이해: 10분
# 구현: 24분
# Debug: -

import sys
from collections import deque

sys.stdin = open("input.txt","r")
tc = int(input())

for _ in range(tc):
    # n=문서개수, m=queue 순서
    n, m = map(int, sys.stdin.readline().split())
    # 우선순위
    lst_prior = deque(list(map(int, sys.stdin.readline().split())))
    idx_q = deque(list(range(n)))

    cnt = 0

    while lst_prior:
        if lst_prior[0] == max(lst_prior):
            cnt += 1
            lst_prior.popleft()
            if idx_q.popleft() == m: print(cnt)
        else:
            lst_prior.rotate(-1)
            idx_q.rotate(-1)