"""
---
title:  "[Python] BOJ_15683_감시"
excerpt: "https://www.acmicpc.net/problem/15683/"
toc: true
toc_sticky: true
toc_label: "Contents"
categories:
  - algorithm
tags:
  - BOJ
  - Implementation
---

문제이해: 분
구현: 분
Debug: 분
참고자료
https://www.landlordgang.xyz/45
"""
import sys
sys.stdin = open("simulation/input.txt", "r")

# 첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)
n, m = map(int, sys.stdin.readline().split())
print(n, m)
arr, cctv, cnt_blks = [], [], 0

# 둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 
# CCTV의 최대 개수는 8개를 넘지 않는다.
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if arr[i][j] == 0: cnt_blks += 1 # 입력 빈칸 세기
        elif 0 < arr[i][j] < 6: cctv.append([i, j, arr[i][j]]) # CCTV 위치, 번호 저장

U, D, R, L = (-1 ,0), (1, 0), (0, 1), (0, -1)

# cctv 빈칸 탐색
visited = [[] for _ in range(len(cctv))]

def detect(idx, lst_dir):
    for d in lst_dir:
        search_blk = set()
        for dr, dc in d:
            r, c = cctv[idx][0], cctv[idx][1]
            while True:
                nr, nc = r + dr, c + dc
                #print(nr, nc)
                if -1 < nr < n and -1 < nc < m:
                    if arr[nr][nc] == 0:
                        search_blk.add((nr, nc))
                        r, c = nr, nc 
                    elif -1 < arr[nr][nc] < 6: r, c = nr, nc #CCTV는 CCTV를 통과할 수 있다. 
                    else: break
                else: break
        visited[idx].append(search_blk) #탐색 완료한 빈칸 좌표 담기


for i in range(len(cctv)):
    if cctv[i][2] == 1: detect(i, [[U], [D], [R], [L]])
    elif cctv[i][2] == 2: detect(i, [[L, R], [U, D]])
    elif cctv[i][2] == 3: detect(i, [[U, R], [U, L], [D, R], [D, L]])
    elif cctv[i][2] == 4: detect(i, [[U, L, R], [U, L, D], [D, L, R], [U, R, D]])
    elif cctv[i][2] == 5: detect(i, [[U, D, L, R]])


maxval = 0

def dfs(depth, graph):
    global maxval
    if depth == len(cctv):
        cnt = len(graph) # 탐색 완료한 빈칸 개수 갱신
        if cnt > maxval: maxval = cnt
        return
    for i in range(len(visited[depth])): dfs(depth+1, graph|visited[depth][i])

dfs(0, set())
print(cnt_blks - maxval)