
"""
---
title:  "[Python] PRGRMS_12941_최솟값_만들기"
excerpt: "https://school.programmers.co.kr/learn/courses/30/lessons/12941"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
  - math
tags:
  - PROGRAMMERS
  - math
---

문제 이해: 5분
구현: 20분
Debug: 12분
참고 자료

예제 코드는 정상 수행했지만. . . 잘못된 logic
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	실패 (2.33ms, 10.3MB)
테스트 3 〉	실패 (2.28ms, 10.2MB)
테스트 4 〉	실패 (2.34ms, 10.3MB)
테스트 5 〉	실패 (2.47ms, 10.2MB)
테스트 6 〉	실패 (2.36ms, 10.2MB)
테스트 7 〉	실패 (2.54ms, 10.3MB)
테스트 8 〉	실패 (2.30ms, 10.3MB)
테스트 9 〉	실패 (2.34ms, 10.3MB)
테스트 10 〉	실패 (2.33ms, 10.2MB)
테스트 11 〉	실패 (0.60ms, 10.2MB)
테스트 12 〉	실패 (0.60ms, 10.2MB)
테스트 13 〉	실패 (0.61ms, 10.2MB)
테스트 14 〉	실패 (0.61ms, 10.2MB)
테스트 15 〉	실패 (0.63ms, 10.1MB)
테스트 16 〉	실패 (0.61ms, 10.1MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
"""

def solution(A, B):
    # 나올 수 있는 최대 값
    answer = (1000 * 1000) * 1000

    # index 처리
    def r_arr(arr):
        arr = [0 for _ in range(len(B))]
        for i in range(len(B)):
            if i == (len(B) - 1):
                tmp = B[-1]
                arr[0] = tmp
                break
            tmp = B[i]
            arr[i + 1] = tmp
        return arr

    # zip 구조 len(A) 가지 경우의 수 생성 (반복)
    for _ in range(len(A)):
        lst_zip = list(zip(A, B))

        e_mult, e_sum = 0, 0
        # 누적합 계산
        for a, b in lst_zip:
            # print(a, b)
            e_mult = a * b
            e_sum += e_mult
        # 최소값 갱신
        answer = min(e_sum, answer)

        rot_B = r_arr(B)
        B = rot_B
        # print(B)

    return answer