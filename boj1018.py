"""
---
title:  "[Python] BOJ_1018_체스판_다시_칠하기"
excerpt: "https://www.acmicpc.net/problem/1018"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - Brute-force search
---

문제 이해: 18분
구현: 25분
Debug: 5분
참고 자료
https://god-gil.tistory.com/62
"""
import sys
sys.stdin = open("input.txt","r")

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline())) for _ in range(n)]

# print(arr)
lst_min_colour = []

# 문제 상황 이해
# 상좌 검 or 상좌 흰 체스판의 경우 모든 체스판을 8x8 이동 탐색할 때
# 64개인 경우는 0
# 32개인 경우는 전부 한 가지 색으로 칠해진 경우

for i in range(n - 7):
    for j in range(m - 7):
        cnt_b, cnt_w = 0, 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0: # 짝수 번째 칸
                    if arr[k][l] == 'W': cnt_w += 1 # 상좌 검 기준, 흰색이 나와야 함
                    else: cnt_b += 1                # 상좌 흰 기준, 검은색이 나와야 함
                else:                # 홀수 번째 칸
                    if arr[k][l] == 'B': cnt_w += 1 # 상좌 검 기준, 흰색이 나와야 함
                    else: cnt_b += 1                # 상좌 흰 기준, 검은색이 나와야 함
        lst_min_colour.append(cnt_b)
        lst_min_colour.append(cnt_w)


print(min(lst_min_colour))