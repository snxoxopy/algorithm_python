k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
"""
chess_map = [
    [0, 0, 2, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 2],
    [0, 2, 0, 0]
]
"""


start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 2 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    # 1. 입력 변수 읽기
    n = len(game_map)
    cnt_turn = 1
    cur_map = [[[] for _ in range(n)] for _ in range(n)]

    # 2. 현재 말들의 좌표 정보 읽기 by using 말 번호
    # 현재 말들의 좌표 정보를 읽어온다.
    # 좌표정보 r, c, d를 어떻게 추출할 것 인가?
    # 각 말 별로 추출해야 함 --> 반복문2
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        # 하나의 말 위에 다른 말을 올릴 수 있다.
        cur_map[r][c].append(i)
        #print(cur_map)

    # 3. 말 이동시키기
    # 말들을 규칙에 맞게 움직이는 부분, Turn --> 반복문1
    while cnt_turn <= 1000:
        # 3-1) 이동 할 때 좌표 읽기
        for horse_idx in range(horse_count):
            r, c, d = horse_location_and_directions[horse_idx]
            nr = r + dr[d]
            nc = c + dc[d]

            # 3-1-1) 좌표 조건: 파란색일 경우
            # 파란색인 경우 말의 이동 방향을 반대로하고 한 칸 이동한다.
            if not 0 <= nr < n or not 0 <= nc < n or game_map[nr][nc] == 2:
                nd = get_d_index_when_go_back(d)

                #horse_location_and_directions[horse_idx][2] = nd
                nr = r + dr[nd]
                nc = c + dc[nd]

                # 방향을 바꾼 후 이동하려는 칸이 파란색인 경우 이동하지 않고 가만히 있는다.
                if not 0 <= nr < n or not 0 <= nc <n or game_map[nr][nc] == 2:
                    continue

            # 3-1-2) 쌓인 말 읽기
            # 같이 이동할 말을 저장하는 변수
            mv_horse_idx_arr = []
            # 현재 좌표에 쌓여있는 말의 개수 만큼 확인
            for i in range(len(cur_map[r][c])):
                cur_stacked_horse_idx_arr = cur_map[r][c][i]

                # 3-1-2-1) 이동해야할 말이 현재 읽어온 쌓인 말 일때
                # 같이 이동할 말 찾기
                # 1) 이동하려는 칸에 말이 이미 있는 경우에 가장 위에 A번 말을 올려놓는다.
                # 2) 현재 옮겨야하는 말은? 현재 말 위의 말들
                if horse_idx == cur_stacked_horse_idx_arr:
                    mv_horse_idx_arr = cur_map[r][c][i:]
                    cur_map[r][c] = cur_map[r][c][:i]
                    break

            # 3-1-3) 좌표 조건: 빨간색 일 경우
            # 빨간색인 경우, 이동 후 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
            if game_map[nr][nc] == 1:
                mv_horse_idx_arr = reversed(mv_horse_idx_arr)

            # 3-1-4) 말 좌표 업데이트
            # 이동해야 할 말들의 좌표 업데이트
            for mv_horse_idx in mv_horse_idx_arr:
                cur_map[nr][nc].append(mv_horse_idx)
                horse_location_and_directions[mv_horse_idx][0], horse_location_and_directions[mv_horse_idx][1] = nr, nc

            # 3-1-5) 종료조건
            if len(cur_map[nr][nc]) >= 4:
                return cnt_turn

        # 3-2) 다음 이동
        cnt_turn += 1

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다