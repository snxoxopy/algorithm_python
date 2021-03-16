from collections import deque

c = 11
b = 2

# 모든 경우의 수 나열이 필요할 경우 BFS
# 동일 시간내 동일 위치에 존재
# 시간은 +1
# 위치는 자유자재로 변함
# 규칙적 -> 배열, 자유자재 -> 딕셔너리
# 각 시간마다 브라운이 갈 수 있는 위치 저장
# [{}]

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]

    # visited[위치][시간]
    # visited[3]에 5라는 키가 있냐? -> 3위치를 5초에 간적 있냐?

    while cony_loc <= 2000000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            cur_pos, cur_time = queue.popleft()

            new_time = cur_time + 1
            new_pos = cur_pos - 1

            if 0 <= new_pos <= 200000:
                visited[new_pos][new_time] = True
                queue.append((new_pos, new_time))

            new_pos = cur_pos + 1
            if 0 <= new_pos <= 200000:
                visited[new_pos][new_time] = True
                queue.append((new_pos, new_time))

            new_pos = cur_pos * 2
            if 0 <= new_pos <= 200000:
                visited[new_pos][new_time] = True
                queue.append((new_pos, new_time))

        time += 1
    # 구현해보세요!
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!