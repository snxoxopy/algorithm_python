# https://www.acmicpc.net/problem/1874
# 문제 이해: 8분
# 구현: 31분
# Debug: 5분

import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip('\n'))
#num = [int(sys.stdin.readline().rstrip('\n')) for _ in range(n)]
#print(num)
#print(n)

oper, stack = [], []
cnt = 1

for _ in range(n):
    num = int(sys.stdin.readline().rstrip('\n'))
    #print(num)
    while cnt < num+1:
        stack.append(cnt)
        #print('push', cnt)
        oper.append('+')
        cnt += 1

    if stack[-1] == num:
        s = stack.pop()
        #print('pop', s)
        oper.append('-')
    else:
        print("NO")
        exit(0)

for i in oper:
    print(i)

