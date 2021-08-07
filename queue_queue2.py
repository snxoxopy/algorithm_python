# https://www.acmicpc.net/problem/18258
# 문제이해: 2분
# 구현: 15분
# Debug: VScode setup 28분

import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().strip())
queue = [sys.stdin.readline().strip() for _ in range(n)]

lst_queue = deque()
for lst_str in queue:
    if "push" in lst_str:
        cmd, value = lst_str.split()
        lst_queue.append(int(value))
    elif "pop" in lst_str:
        print(lst_queue.popleft()) if lst_queue else print('-1')
    elif "front" in lst_str:
        print(lst_queue[0]) if lst_queue else print('-1')
    elif "back" in lst_str:
        print(lst_queue[-1]) if lst_queue else print('-1')
    elif "empty" in lst_str:
        print("1") if not lst_queue else print("0")
    elif "size" in lst_str:
        print(len(lst_queue))