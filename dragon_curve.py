import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
# input
n = int(input())
# arr = [c, r, d, g]
# r c는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다.
arr = [list(map(int, input().split())) for _ in range(n)]
# 0: c좌표가 증가하는 방향 (→)
# 1: r좌표가 감소하는 방향 (↑)
# 2: c좌표가 감소하는 방향 (←)
# 3: r좌표가 증가하는 방향 (↓)
# dir = ((0, 1), (-1, 0), (0, -1), (1, 0))
dr = (0, -1, 0, 1)
dc = (1, 0, -1, 0)


pos_rect = []

# system

results = [[False] * 101 for _ in range(101)] # 정사각형 지도 초기화
num_rect = 0

def cnt_rect(results):
    global num_rect
    for i in range(100):
        for j in range(100):
            if results[i][j] and results[i][j+1] and results[i+1][j] and results[i+1][j+1]:
                num_rect += 1

# main
rotate = deque()
for i in range(n):
    c, r, d, g = arr[i]
    pos_rect.append([r, c])
    rotate.append(d)
    for _ in range(g):
        reverse = list(reversed(rotate))
        for j in reverse:
            if j + 1 == 4: rotate.append(0)
            else: rotate.append(j + 1)

    while rotate:
        results[r][c] = True
        cw = rotate.popleft()
        nr, nc = r + dr[cw], c + dc[cw]
        if -1 < nr < 101 and -1 < nc < 101:
            pos_rect.append([nr, nc])
            results[nr][nc] = True
            r, c = nr, nc

# output
# 첫째 줄에 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력한다.
# 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수
cnt_rect(results)
print(num_rect)
