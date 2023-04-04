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
        print(s, str_s)
        if s == str_s:
            return True
        return False

        ans1, ans2 = 0, 0

        for i in range(len(s), -1, -1):
            print("forward", s[:i])
            if(isPalindrome(s[:i])):
                ans1 = i
                break

        for j in range(len(s)):
            if(isPalindrome(s[j:len(s)])):
                ans2 = len(s) - j
                break

        answer = max(ans1, ans2)

        return answer
