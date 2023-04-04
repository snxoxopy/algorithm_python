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
  - Implementation
---

문제 이해: 3분
구현: 70분
Debug: 분
참고 자료:
"""

def solution(s):
    answer = 0

    def isPalindrome(s):
        str_s = ""
        for i in range(len(s) - 1, -1, -1):
            str_s += s[i]
        # print(s, str_s)
        if s == str_s:
            return True
        return False

    for diff in range(len(s), -1, -1):
        for start_s in range((s)):
            if(isPalindrome(s[start_s:start_s+diff])):
                answer = max(answer, len(s[start_s:start_s+diff]))
                break

        return answer
