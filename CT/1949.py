from collections import deque
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

n, k = map(int, input().split())
# print(n, k)
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# print(arr)

# max_num 좌표 max_pos
max_num, q_pos = 0, deque()

max_num = max(max(arr[:]))
# print(max_num)

for r in range(n):
    for c in range(n):
        if arr[r][c] == max_num:
            q_pos.append((r, c))
# print(q_pos)

def is_k(k, arr, nr, nc, target):
    global k_cnt
    if arr[nr][nc] - k < target and k_cnt == 1:
        arr[nr][nc] -= k
        k_cnt = 0
        return True
    return False

dr = (0, -1, 0, 1)
dc = (1, 0, -1, 0)


# dfs

def dfs(_r, _c, arr, k, answer, max_ans, visited):
    # q = deque((r, c))

    for d in range(4):
        nr, nc = _r + dr[d], _c + dc[d]
        if -1 < nr < n and -1 < nc < n and not visited[nr][nc]:
            if arr[nr][nc] < target or is_k(k, arr, nr, nc, target):
                # answer += 1
                visited[nr][nc] = 1
                dfs(nr, nc, arr, k, answer, max_ans, visited)
                visited[nr][nc] = 0
                # answer -= 1
        # print(sum([sum(i) for i in visited]))
        max_ans = max(sum([sum(i) for i in visited]), max_ans)
    return max_ans


max_num = 0
for r, c in q_pos:
    target = arr[r][c]
    q = deque([[r, c]]) # 등산로 길이 계산 좌표
    visited = [[0] * n for _ in range(n)]

    visited[r][c] = 1
    k_cnt = 1
    answer = 0
    max_num = max(max_num, dfs(r, c, arr, k, answer, 0, visited))



print(max_num)

