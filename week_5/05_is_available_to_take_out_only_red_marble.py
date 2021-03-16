from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

    #남, 동, 북, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

#큐를 탐색하기 위한 함수 -> 매 방향으로 이동하는 것을 계산
#큐에서 꺼낸 빨간 구슬과 파랑 구슬의 위치 이용
def move_until_or_hole(r, c, diff_r, diff_c, game_map):
    mv_cnt = 0

    while game_map[r+diff_r][c+diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        mv_cnt += 1

    return r, c, mv_cnt


def is_available_to_take_out_only_red_marble(game_map):
    # 구현해보세요!
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    red_r, red_c, blue_r, blue_c = -1, -1, -1, -1

    #game_map "R", "B"이 나오면 인덱스 정보 저장
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_r, red_c = i, j
            elif game_map[i][j] == "B":
                blue_r, blue_c = i, j

    #"R", "B" 인데스 정보를 queue에 저장
    queue.append((red_r, red_c, blue_r, blue_c, 1))

    #현재 빨간구슬과 파란 구슬의 위치 방문 처리
    visited[red_r][red_c][blue_r][blue_c] = True
    
    while queue:
        red_r, red_c, blue_r, blue_c, try_cnt = queue.popleft() #FIFO
        if try_cnt > 10:
            break

        for i in range(4):
            next_red_r, next_red_c, r_cnt = move_until_or_hole(red_r, red_c, dr[i], dc[i], game_map)
            next_blue_r, next_blue_c, c_cnt = move_until_or_hole(blue_r, blue_c, dr[i], dc[i], game_map)

            #파란 구슬이 구멍에 떨어지지 않으면
            if game_map[next_blue_r][next_blue_c] == 'O':
                continue

            #빨간 구슬이 구멍에 떨어진다면
            if game_map[next_red_r][next_red_c] == 'O':
                return True

            #빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
            if next_red_r == next_blue_r and next_red_c == next_blue_c:
                #이동 거리가 많은 구슬을 한칸 뒤로
                if r_cnt > b_cnt:
                    next_red_r -= dr[i]
                    next_red_c -= dc[i]
                else:
                    next_blue_r -= dr[i]
                    next_blue_c -= dc[i]

            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_red_r][next_red_c][next_blue_r][next_blue_c]:
                visited[next_red_r][next_red_c][next_blue_r][next_blue_c] = True
                queue.append((next_red_r, next_red_c, next_blue_r, next_blue_c, try_cnt + 1))
        return False

print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다