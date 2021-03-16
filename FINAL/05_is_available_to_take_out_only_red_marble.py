from collections import deque

# '.'은 빈 칸을 의미하고,
# '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며,
# 'O'는 구멍의 위치를 의미한다.
game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]


# Outcomes
# 파란 구슬이 구멍에 빠지면 실패이다.
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패
# 빨간 구슬이 구멍에 빠지면 성공
# 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지

# Events
# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기
# 남 동 북 서 -> 4
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def mv_until_wall(r, c, diff_r, diff_c, game_map):
    cnt_mv = 0

    # 벽이 아니거나 구멍이 아닐 때 까지
    while game_map[r + diff_r][c + diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        cnt_mv += 1

    return r, c, cnt_mv

def is_available_to_take_out_only_red_marble(game_map):
    # 0. 알고리즘, 자료구조 정하기
    # 알고리즘: BFS -> 공 2개에 대한 각 visited 필요 -> 2d List * 2개 -> 4d List
    # 자료구조: Queue -> 공 2개에 대한 좌표와 탐색 횟수를 저장한다.

    # Array
    # >> > [[False] * 4 for _ in range(3)]
    # [[False, False, False, False], [False, False, False, False], [False, False, False, False]]
    #
    # Array
    # >> > [[[] for _ in range(4)] for _ in range(3)]
    # [[[], [], [], []], [[], [], [], []], [[], [], [], []]]
    #
    # List
    # >> > [[] for _ in range(4) for _ in range(3)]
    # [[], [], [], [], [], [], [], [], [], [], [], []]

    # 1. 입력변수 선언
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    red_r, red_c, blue_r, blue_c = -1, -1, -1, -1


    # 2. 구슬 좌표 읽기
    for i in range(n):
        for j in range(m):
            # 2-1) R 구슬 좌표 찾기
            if game_map[i][j] == "R":
                red_r, red_c = i, j
            # 2-2) B 구슬 좌표 찾기
            elif game_map[i][j] == "B":
                blue_r, blue_c = i, j

    # 3. R좌표, B좌표, 수행 횟수 저장
    queue.append((red_r, red_c, blue_r, blue_c, 1))

    # 4. 방문처리
    visited[red_r][red_c][blue_r][blue_c] = True

    # 5. BFS with queue
    while queue:
        # 5-1) queue를 BFS한다. 목적: B, R 좌표 경우의 수 확인
        red_r, red_c, blue_r, blue_c, cnt_try = queue.popleft() #FIFO

        # 5-2) 반복문 종료조건
        if cnt_try > 10:
            break

        # 5-3) 좌표 이동 4가지 경우의 수 확인
        for i in range(len(dr)):
            # 5-3-1) 좌표 업데이트
            red_nr, red_nc, cnt_r = mv_until_wall(red_r, red_c, dr[i], dc[i], game_map)
            blue_nr, blue_nc, cnt_b = mv_until_wall(blue_r, blue_c, dr[i], dc[i], game_map)

            # 5-3-2) 실패X 성공X: 파란 구슬이 구멍에 떨어지면 -> 파란 구슬이 구멍에 떨어지지 않으면 실패x, 성공x
            if game_map[blue_nr][blue_nc] == 'O':
                # continue의 아래 코드 수행하지 않고 반복문의 다음 인덱스 조회
                continue

            # 5-3-3) 성공O: 빨간 구슬이 구멍에 떨어지는 경우
            if game_map[red_nr][red_nc] == 'O':
                return True

            # 5-3-4) 빨간 구슬과 파란 구슬이 동시에 같은 칸일 경우
            if red_nr == blue_nr and red_nc == blue_nc:
                # 5-3-4-1) 이동거리가 많은 구슬 한칸 이동
                if cnt_r > cnt_b:
                    # 이전좌표 복귀
                    red_nr -= dr[i]
                    red_nc -= dc[i]
                else:
                    blue_nr -= dr[i]
                    blue_nc -= dc[i]

            # 5-3-5) BFS 탐색을 마치고 방문 여부 확인
            if not visited[red_nr][red_nc][blue_nr][blue_nc]:
                visited[red_nr][red_nc][blue_nr][blue_nc] = True
                queue.append((red_nr, red_nc, blue_nr, blue_nc, cnt_try+1))

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다