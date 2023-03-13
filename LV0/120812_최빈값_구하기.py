"""
https://school.programmers.co.kr/learn/courses/30/lessons/120812
"""

def solution(array):
    # array.sort()
    answer = 0
    cnt = [0 for _ in range(1000)]
    # cnt = dict()
    for num in array:
        cnt[num] += 1
    # print(cnt)
    s_cnt = sorted(cnt)
    # print(s_cnt)
    # if len(array) == 1: answer = 1 # 이해 안감
    if s_cnt[-1] == s_cnt[-2]: answer = -1
    else:
        # answer = s_cnt[-1]
        for i in range(0, 1000):
            if cnt[i] == 0: continue
            if cnt[i] == s_cnt[-1]:
                answer = i
    return answer