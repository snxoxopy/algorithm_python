# https://www.acmicpc.net/problem/4949
# 문제 이해: 10분
# 구현: 60분
# Debug: 16분

import sys


def check_parenthesis(s):
    stack = []
    for i in s:
        if i == "(" or i == "[": stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(': return False
            stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[': return False
            stack.pop()

    if stack: return False
    return True


while True:
    s = sys.stdin.readline().rstrip('\n')
    if s == ".": break
    print('yes') if check_parenthesis(s) else print('no')



