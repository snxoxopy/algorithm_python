import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    #0. 알고리즘, 자료구조 정하기
    #알고리즘: 조합에 대한 모든 경우의 수에서 최소 거리 계산
    #자료구조: List

    #1. 입력변수 선언
    chicken_loca_list = []
    home_loca_list = []

    #2. 초기값 읽기
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_loca_list.append([i,j])
            if city_map[i][j] == 2:
                chicken_loca_list.append([i,j])

    #3. 조합 탐색
    chicken_loca_m_comb = list(itertools.combinations(chicken_loca_list, m))
    min_dist_m_comb = sys.maxsize
    for comb_chicken in chicken_loca_m_comb:
        dist = 0
        for home_r, home_c in home_loca_list:
            min_dist = sys.maxsize
            for chicken_loca in comb_chicken:
                min_dist = min(min_dist, abs(home_r-chicken_loca[0]) + abs(home_c-chicken_loca[1]))
            dist += min_dist
        min_dist_m_comb = min(min_dist_m_comb, dist)

    return min_dist_m_comb


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!