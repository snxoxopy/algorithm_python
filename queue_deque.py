# https://www.acmicpc.net/problem/10866
# 문제이해: 3분
# 구현: 12분
# Debug: 5분

import sys
from collections import deque

sys.stdin = open("input.txt","r")

tc = int(input())
deq_q = deque()

for i in range(tc):
    cmd = sys.stdin.readline().strip()
    q = cmd.split()

    if "push_back" == q[0]: deq_q.append(int(q[1]))
    elif "push_front" == q[0]: deq_q.appendleft(int(q[1]))
    elif "front" == q[0]: print(deq_q[0] if deq_q else -1)
    elif "back" == q[0]: print(deq_q[-1] if deq_q else -1)
    elif "size" == q[0]: print(len(deq_q))
    elif "empty" == q[0]: print("0") if deq_q else print("1")
    elif "pop_front" == q[0]: print(deq_q.popleft() if deq_q else -1)
    elif "pop_back" == q[0]: print(deq_q.pop() if deq_q else -1)