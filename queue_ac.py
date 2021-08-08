# https://www.acmicpc.net/problem/5430
# 문제이해: 12분
# 구현: 24분
# Debug: 30분

import sys
from collections import deque
import timeit

sys.stdin = open("queue/input.txt", "r")
t_start = timeit.default_timer()
p = int(sys.stdin.readline().strip())

for _ in range(p):
    cmds = sys.stdin.readline().strip()
    tc = int(sys.stdin.readline().strip())
    lst_num = sys.stdin.readline()
    q = deque(map(int,lst_num.rstrip()[1:-1].split(','))) if tc != 0 else deque([])
    isReverse, isError = False, False
    for cmd in cmds:
        if 'R' == cmd:
            isReverse = not isReverse
        else:
            if q and q[0] != '':
                q.pop() if isReverse else q.popleft()
            else:
                isError = True
                break
    if isError: print("error")
    else:
        if isReverse: q.reverse()
        print("[", end='')
        for i in range(len(q)):
            if i == len(q)-1:
                print(str(q[i]),end='')
            else:
                print(q[i],end=',')
        print("]")

t_end = timeit.default_timer()
print("소요시간 = %f[ms]" %((t_end-t_start)*1000))