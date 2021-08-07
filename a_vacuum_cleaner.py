# https://www.acmicpc.net/problem/14503
# 문제이해: 11분
# 구현: 32분
# Debug: 5분
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
# 첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)
n, m = map(int, sys.stdin.readline().split())
# 둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다.
init_r, init_c, init_d = map(int, sys.stdin.readline().split())
# d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

#print(init_r, init_c, init_d)

# 셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로,
# 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다.
# 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.
lst_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#print(lst_map)


# 1. 현재 위치를 청소한다.
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
#   왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
#   왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
#   네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
#   네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.


def turn_left(d):
    # 북 동 남 서
    # 서 북 동 남
    # 0 -> 3
    # 1 -> 0
    # 2 -> 1
    # 3 -> 2
    d = d - 1 if d > 0 else 3
    return d

def go_back(d):
    # 0 -> 2
    # 1 -> 3
    # 2 -> 0
    # 3 -> 1
    return (d + 2) % 4

q = deque([[init_r, init_c, init_d]])
#print(q)
cnt = 1
lst_map[init_r][init_c] = 2

while q:
    r, c, d = q.popleft()
    tmp_d = d

    for i in range(4):
        tmp_d = turn_left(tmp_d)
        nr, nc = r + dr[tmp_d], c + dc[tmp_d]

        if -1 < nr < n and -1 < nc < m and lst_map[nr][nc] == 0:
            cnt += 1
            lst_map[nr][nc] = 2
            q.append([nr, nc, tmp_d])
            break

        elif i == 3:
            nr, nc = r + dr[go_back(d)], c + dc[go_back(d)]
            q.append([nr, nc, d])

            if lst_map[nr][nc] == 1:
                print(cnt)
                exit(0)

# 로봇 청소기가 청소하는 칸의 개수를 출력한다.