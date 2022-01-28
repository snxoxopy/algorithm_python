"""
---
title:  "[Python] BOJ_1436_영화감독_숌"
excerpt: "https://www.acmicpc.net/problem/1436"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - Brute-force search
---

문제 이해: 5분
구현: 분
Debug: 분
참고 자료
https://hongcoding.tistory.com/108?category=940557
"""
import sys
sys.stdin = open("input.txt")

n = int(sys.stdin.readline())

# N 번째 작은 666 포함 숫자
# # N = 6
# 5666
# # N = 7
# 6666 (X)
# 6660 (O)

n_start = 665 # 초기값 666이면 N=1일 때, 1666이 나오므로 주의!

while n:
    n_start += 1
    if "666" in str(n_start): n -= 1
    # print(n_start)

print(n_start)

"""
while n: # n이 0일 때 종료, n = 1인 경우 667까지 계산이 되므로 추후에 빼주어야함
    if "666" in str(n_start): n -= 1
    n_start += 1
    # print(n_start)

print(n_start)
"""