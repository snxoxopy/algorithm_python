# https://www.acmicpc.net/problem/10828
# doubly-ended-queue의 약자
# 맨 앞과 뒤에 데이터를 삽입하고 삭제할 수 있게 해주는 자료형

from collections import deque

# 맨 끝 데이터 삭제
import sys
sys.stdin = open('input.txt','r')
n = int(input())
stk = []
for _ in range(n):
    x = list(map(str,input().split()))
    if x[0] =='push':
        stk.append(int(x[1]))
    elif x[0] =='pop':
        if stk:
            print(stk.pop())
        else:
            print('-1')
    elif x[0] =='size':
        print(len(stk))
    elif x[0] =='empty':
        if stk:
            print('0')
        else:
            print('1')
    elif x[0] =='top':
        if stk:
            print(stk[-1])
        else:
            print('-1')