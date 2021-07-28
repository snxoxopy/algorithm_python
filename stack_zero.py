# https://www.acmicpc.net/problem/10773
# 문제 이해 8분
# 구현 7분
import sys

sys.stdin = open("input.txt", "r")
k = int(input())
arr = [0]
#print(arr)


for _ in range(k):
    data = int(input())
    #print(data)
    arr.append(data) if data else arr.pop()

print(sum(arr))