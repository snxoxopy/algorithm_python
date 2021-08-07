# https://www.acmicpc.net/problem/1021
# 문제이해: 3분
# 구현: 31분
# Debug: -

# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
# 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

import sys
from collections import deque

sys.stdin = open("input.txt","r")

n, m = map(int, sys.stdin.readline().strip().split())
#print(n, m)
lst_idx = list(map(int, sys.stdin.readline().strip().split()))
#print(lst_idx)

q = deque([i for i in range(1, n+1)])

cnt = 0

for idx in lst_idx:
    while True:
        if q[0] == idx:
            q.popleft()
            break
        else:
            if q.index(idx) <= len(q)//2:
                q.rotate(-1)
                cnt += 1
            else:
                q.rotate(1)
                cnt += 1

print(cnt)
