from collections import deque


def hide_n_seek(me, bro):
    cnt = 0
    queue = deque([[me, cnt]])
    visited = [False] * 100001
    while queue:
        v = queue.popleft()
        i = v[0]
        cnt = v[1]
        if not visited[i]:
            visited[i] = True
            if i == bro: return cnt
            cnt += 1
            if 0 <= i * 2 <= 100000: queue.append([i * 2, cnt])
            if 0 <= i + 1 <= 100000: queue.append([i + 1, cnt])
            if 0 <= i - 1 <= 100000: queue.append([i - 1, cnt])

    return cnt

n, k = map(int, input().split())
print(hide_n_seek(n, k))
