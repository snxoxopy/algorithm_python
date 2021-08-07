# https://www.acmicpc.net/problem/17298

# 문제 이해: 3분
# 구현: 42분
# Debug: -

import sys

sys.stdin = open("input.txt", "r")

n = int(input())
lst_num = list(map(int, input().split()))
stack = []
ans = [-1 for _ in range(n)]

for idx in range(len(lst_num)):
    while stack and lst_num[idx] > lst_num[stack[-1]]:
        ans[stack.pop()] = lst_num[idx]

    stack.append(idx)

print(*ans)