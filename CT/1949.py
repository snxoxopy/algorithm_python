# 문제: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 참고: https://chelseashin.tistory.com/2

import sys

sys.stdin = open("sample_input.txt", "r")


# dfs
dr = (0, -1, 0, 1)
dc = (1, 0, -1, 0)
def dfs(_r, _c, chance):
    global max_num, visited
    max_num = max(max_num, visited[_r][_c])
    for d in range(4):
        nr, nc = _r + dr[d], _c + dc[d]
        # target = arr[_r][_c]
        if -1 < nr < n and -1 < nc < n and not visited[nr][nc]:
            if arr[nr][nc] < arr[_r][_c]:
                visited[nr][nc] = visited[_r][_c] + 1
                dfs(nr, nc, chance)
                visited[nr][nc] = 0
            elif chance and arr[nr][nc] - k < arr[_r][_c]:
                tmp = arr[nr][nc]
                arr[nr][nc] = arr[_r][_c] - 1
                visited[nr][nc] = visited[_r][_c] + 1
                dfs(nr, nc, chance - 1)
                visited[nr][nc] = 0
                arr[nr][nc] = tmp


# main
T = int(input())
for test_case in range(1, T + 1):
    # output
    max_num = 0

    # input
    n, k = map(int, input().split())
    # print(n, k)
    arr = []
    max_top = 0
    for i in range(n):
        arr.append(list(map(int, input().split())))
        for j in range(n):
            if arr[i][j] > max_top: max_top = arr[i][j]

    # print(arr)

    # max_top: 정상
    # max_top = max(max(arr)) -> 오답 주의 사용 금지
    # print(max_top)

    visited = [[0] * n for _ in range(n)]
    # k_cnt = 1
    for r in range(n):
        for c in range(n):
            if arr[r][c] == max_top:
                visited[r][c] = 1
                dfs(r, c, 1)
                visited[r][c] = 0

    print("#{} {}".format(test_case, max_num))
