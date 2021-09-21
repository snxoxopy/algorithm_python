"""
---
title:  "[Python] BOJ_20057_마법사 상어와 토네이도"
excerpt: "https://www.acmicpc.net/problem/20057"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - Implementation
---

문제이해: 분
구현: 분
Debug: 분
참고자료
"""

import sys

sys.stdin = open("input.txt", "r")


# 첫째 줄에 격자의 크기 N이 주어진다. 
n = int(sys.stdin.readline())

# 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습하려고 한다. 
# 둘째 줄부터 N개의 줄에는 격자의 각 칸에 있는 모래가 주어진다. 
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#test done
#print(n)
#print(arr)


# 가운데 칸부터 토네이도의 이동이 시작된다.
# 토네이도는 한 번에 한 칸 이동한다. 
# 토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.

# 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다. 
rate = [
    [0, 0, 2, 0, 0],
    [0, 10, 7, 1, 0],
    [5, 'a', 0, 0, 0],
    [0, 10, 7, 1, 0],
    [0, 0, 2, 0, 0]
]


# 좌 > 하 > 우 > 상
dr, dc = (0, 1, 0, -1), (-1, 0, 1, 0)

# 좌 > 하 > 우 > 우 > 상 > 상 > 좌 > 좌 > 좌 > 하 > 하 > 하 > 우 > 우 > 우 > 우
# 1 > 1 > 2 > 2 > 3 > 3 > 4
# 방향이 하, 상 이후 이동 횟수 1씩 증가

def rotate_ccw(arr):
    tmp = [[0] * 5 for _ in range(5)]
    # 비율이 
    for i in range(5):
        for j in range(5):
            tmp[4 - j][i] = arr[i][j]
    return tmp

# test done
# test = rotate_ccw(pro)
# print('test',test)


# 모래 양 계산
def tornado(nr, nc, arr, rate, ans):
    # 현재 탐색 좌표에서 rate array의 시작 좌표로 이동
    off_r, off_c = nr - len(rate)//2, nc - len(rate)//2
    tmp, len_rate = 0, len(rate)
    # rate array * array
    for i in range(len_rate):
        for j in range(len_rate):
            # 비율이 존재하는 영역이
            if rate[i][j] != 'a' and rate[i][j] != 0:
                # 격자 안에 존재한다면 
                # (i + off = 비율의 배열을 전체 격자의 절대 좌표로 치환)
                if -1 < i + off_r < n and -1 < j + off_c < n:
                    # 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다.
                    # y*rate
                    # 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다. 
                    arr[i + off_r][j + off_c] += arr[nr][nc] * rate[i][j] // 100
                else: ans += arr[nr][nc] * rate[i][j] // 100 #격자를 벗어난 경우
                # α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다. 
                # alaph == y - y*rate
                # 비율이 존재하는 영역에 대한 모래 양의 합
                tmp += arr[nr][nc] * rate[i][j] // 100
            elif rate[i][j] == 'a': alpha = (i, j)
    # alpha의 절대 좌표가 범위 내 존재한다면
    if -1 < alpha[0] + off_r < n and -1 < alpha[1] + off_c < n:
        # 비율이 적혀있는 칸으로 이동하지 않은 남은 모래양 = 비율이 존재하지 않는 영역의 모래양
        # = 현재 좌표의 모래양 - 비율이 존재하는 영역 모래 양의 합
        arr[alpha[0] + off_r][alpha[1] + off_c] += arr[nr][nc] - tmp
    else: ans += arr[nr][nc] - tmp # alpha 절대 좌표가 범위를 벗어날 경우, 격자 바깥으로 나간 모래양
    return arr, ans


# ================================================================= main
tr, tc = n // 2, n // 2
ans, flag, turn = 0, 1, 1
while flag != 0:
    # 모래가 격자의 밖으로 이동할 수도 있다. 
    for d in range(len(dr)):
        for j in range(turn):
            tr, tc = tr + dr[d], tc + dc[d]
            if -1 < tr < n and -1 < tc < n:
                arr, ans = tornado(tr, tc, arr, rate, ans)
            if d == 1 or d == 3:
                if j == 0: turn += 1 #하, 상 이동 후 이동량 증가
            if (tr, tc) == (0, 0): flag = 0 # 토네이도는 (1, 1)까지 이동한 뒤 소멸한다. 
        #토네이도가 상/하/좌/우 방향이 바뀔 때마다 반시계 방향으로 회전한다.
        rate = rotate_ccw(rate)
    # 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양을 구해보자.
    # if flag == 0: break

# r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.
# 격자의 밖으로 나간 모래의 양을 출력한다.
print(ans)

