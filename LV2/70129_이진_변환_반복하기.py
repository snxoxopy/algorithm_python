
"""
---
title:  "[Python] PRGRMS_70129_이진_변환_반복하기"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/70129"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - PROGRAMMERS
  - implementation
---

문제 이해: 5분
구현: 20분
Debug: 6분
참고 자료:

"""
# 1 개수 세기
def rmv_zero(s):
    cnt = 0
    for c in s:
        if c != '0':
            cnt += 1
    return cnt


# 이진수 거꾸로 넣기
def make_bin(cnt):
    answer = str()
    while cnt != 0:
        answer += str(cnt % 2)
        # answer = [], answer.append(cnt%2) -> 이 방법은 len(s) 단계에서 문제 발생함
        cnt //= 2
    return answer


def solution(s):
    answer = []
    cnt_bin = 0
    sum_zero = 0

    while (True):
        cnt_one = rmv_zero(s)
        sum_zero += (len(s) - cnt_one)
        s = make_bin(cnt_one)
        cnt_bin += 1
        if cnt_one == 1: break
    answer = [cnt_bin, sum_zero]
    return answer