"""
---
title:  "[Python] BOJ_20055_청소년 상어"
excerpt: "https://www.acmicpc.net/problem/20055"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - Implementation
---
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")


# 길이가 N인 컨베이어 벨트가 있고,
# 길이가 2N인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있다.


# 첫째 줄에 N, K가 주어진다.
n, k = map(int, sys.stdin.readline().split())
#print(n, k)
# 둘째 줄에는 A1, A2, ..., A2N이 주어진다.
arr = deque(map(int, sys.stdin.readline().split()))
#print(arr)
# 값 내구도
# 로봇 유무 위치 확인
robot = deque([0] * n)

# i번 칸의 내구도는 Ai이다.
# 위의 그림에서 1번 칸이 있는 위치를 "올리는 위치",
# N번 칸이 있는 위치를 "내리는 위치"라고 한다.


cnt, time = 0, 0
while cnt < k:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    arr.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있다.
    # 로봇은 올리는 위치에만 올릴 수 있다. 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    # 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.
    # 로봇이 없고 내구도가 1 이상일 때, 해당 자리의 내구도 감소하고 로봇을 위치한다.

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    #    로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    # 배열의 마지막 직전 부터 올라타는 지점까지 로봇이 올라탈 수 있는지 확인하는 반복문
    #for i in range(n-2, -1, -1): # X
    # 로봇 이동
    for i in range(-2, -n-1, -1): # 로봇 내리기 직전, 내릴 때
        if robot[i] == 1 and robot[i + 1] == 0 and arr[i + 1 - n] > 0:
            robot[i], robot[i + 1] = 0, 1
            arr[i + 1 - n] -= 1

    # 로봇 이동 후 내리는 위치 비우기
    robot[-1] = 0

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if robot[0] == 0 and arr[0] > 0:
        robot[0] = 1
        arr[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    cnt = arr.count(0)
    time += 1

print(time)
# 몇 번째 단계가 진행 중일때 종료되었는지 출력한다.
