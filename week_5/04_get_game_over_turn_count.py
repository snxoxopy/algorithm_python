k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 파란색을 만나서 반대로 가야하는 경우
# 0 -> 1
# 1 -> 0
# 2 -> 3
# 3 -> 2
# 홀수 -1, 짝수 +1
def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(chess_map)
    current_stacked_horse_map = [
        [
            [] for _ in range(n)
        ] for _ in range(n)
    ]
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)
    turn_cnt = 1
    while turn_cnt <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]
            #파란색 이거나 범위를 벗어났을 때
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)

                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                #막히면 안감
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            mv_horse_idx_arr = []
            for i in range(len(current_stacked_horse_map[r][c])):
                current_stacked_horse_idx = current_stacked_horse_map[r][c][i]
                if horse_index == current_stacked_horse_idx:
                    mv_horse_idx_arr = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break

            if game_map[new_r][new_c] == 1:
                mv_horse_idx_arr = reversed(mv_horse_idx_arr)

            for mv_horse_idx in mv_horse_idx_arr:
                current_stacked_horse_map[new_r][new_c].append(mv_horse_idx)
                horse_location_and_directions[mv_horse_idx][0],horse_location_and_directions[mv_horse_idx][1] = new_r, new_c
            # 종료조건: 말이 4개 이상 쌓인 경우
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_cnt
        turn_cnt += 1

    print(current_stacked_horse_map)
    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다