"""
---
title:  "[Python] PRGRMS_12904_가장_긴_팰린드롬"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/12904"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - PROGRAMMERS
  - DP
---

문제 이해: 3분
구현: 70분
Debug: 분
참고 자료:
https://velog.io/@hyunjong96/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC
"""


def solution(s):
    answer = 0
    len_s = len(s)
    # dp = [[0]*len_s]*len_s
    dp = [[0 for _ in range(len_s)] for _ in range(len_s)]
    # print(dp)

    for i in range(len_s):
        # print(i)
        dp[i][i] = 1
        # print(dp)
        answer = 1
    # print(dp)

    for i in range(len_s - 1):
        if (s[i] == s[i + 1]):
            # print(s[i], s[i+1])
            dp[i][i + 1] = 1

    # print(dp)

    for width in range(3, len_s + 1):
        # print(width)
        for i in range(len_s + 1):
            if i + width == (len_s + 1): break
            j = i + width - 1
            # print("width, i, j = ", width, i, j)

            if (s[i] == s[j] and dp[i + 1][j - 1]):
                dp[i][j] = 1
                answer = width

    return answer
