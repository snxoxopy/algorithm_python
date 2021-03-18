from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def escape_mazes(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if graph[nr][nc] == 0:
                continue
            if graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1
                queue.append((nr, nc))

    return graph[n-1][m-1]


print(escape_mazes(0,0))