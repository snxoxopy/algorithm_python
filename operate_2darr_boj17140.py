"""
---
title:  "[Python] BOJ_17140_이차원_배열과_연산"
excerpt: "https://www.acmicpc.net/problem/17140"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - Implementation
  - Sort
---

문제이해: 17분
구현: 60분
Debug: 12분
참고자료
https://velog.io/@djagmlrhks3/Algorithm-BaekJoon-17140.-%EC%9D%B4%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4%EA%B3%BC-%EC%97%B0%EC%82%B0-by-Python
https://www.daleseo.com/python-zip/
"""

import sys

sys.stdin = open("input.txt","r")
r, c, k = map(int, sys.stdin.readline().split())

# 크기가 3×3인 배열 A가 있다
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]


def cal(arr, type):
    print("cal", type)
    
    # 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다.
    max_lst, arr_sorted = 0, []
    for row in arr:
        lst_sorted, arr_append = [], []
        # 수의 개수 세기위해 고유값 추출
        for num in set(row):
            # 수를 정렬할 때 0은 무시해야 한다. 
            if num == 0: continue
            cnt = row.count(num)
            lst_sorted.append([num, cnt])

            # 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다. 
            # 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 
        lst_sorted = sorted(lst_sorted, key = lambda x: [x[1], x[0]]) #O(NlogN)
        

        for num, cnt in lst_sorted:
            arr_append += [num, cnt]
        arr_sorted.append(arr_append)
        # 가장 긴 list 길이 세기
        max_lst = max(len(arr_append), max_lst)
        #print('max_lst',max_lst)

    for row_sorted in arr_sorted:
        # 행 또는 열의 크기가 커진 곳에는 0이 채워진다.
        row_sorted += [0] * (max_lst - len(row_sorted))
        if len(row_sorted) > 100:
            # 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
            row_sorted = row_sorted[:100]


    print('arr_sorted = ',arr_sorted)
    if type == "R": 
        return arr_sorted
    else:
        return list(zip(*arr_sorted))

        

# 1초가 지날때마다 배열에 연산이 적용된다.    
time = 0
while True:
    # 100초가 지나도 A[r][c] = k가 되지 않으면 -1을 출력한다.
    if time > 100:
        time = -1
        break
    # 배열의 인덱스는 1부터 시작한다. 
    # 예제 6 반례, 범위 벗어나는지 확인
    if -1 < r-1 < len(arr) and -1 < c-1 < len(arr[0]) and arr[r-1][c-1] == k:
        break

    # 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
    # * 위 조건은 함수내부에서 구현하는게 더 편함

    # 연산은 동일, 배열의 모양을 바꾸기
    # dict 사용!
    # dict(*arr) -> 전치행렬 로띠언니 위클리챌린지 2주차 코드 참고

    if len(arr) >= len(arr[0]):
        # R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 
        # 행의 개수 ≥ 열의 개수인 경우에 적용된다.
        arr = cal(arr, "R")
    else:
        # C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다.
        # 행의 개수 < 열의 개수인 경우에 적용된다.
        arr = cal(list(zip(*arr)), "C")
        
    time += 1

print(time)