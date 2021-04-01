import sys
sys.stdin = open('input.txt','r')
#input
n, l = map(int, input().split())
arr = []
for _ in range(n): arr.append(list(map(int, input().split())))
ans = 0
#print(arr)

#system
# Counter >= 0 지나감
#   1. 같은 높이 길
#   2. 경사로 상승길
#         이전에 길이 l 경사로가 만들어져 있어야 함 -> cnt >= l
#         cnt = 1 초기화
#   3. 경사로 하강길
#         앞으로 길이 l 경사로를 만들어야 함
#         cnt = -l + 1 -> cnt < 0 경우, 경사로 만들 수 없음
# Counter < 0 못 지나감
#   위 3가지 경우에 해당하지 않는 경우

# 가로방향 탐색
for i in range(n):
    cnt = 1
    prev = arr[i][0]
    for j in range(1, n):
        if arr[i][j] == prev:
            cnt += 1
        elif arr[i][j] == prev + 1:
            if cnt >= l:
                cnt = 1
                prev = arr[i][j]
            else: break
        elif arr[i][j] == prev - 1:
            if cnt >= 0:
                cnt = -l + 1
                prev = arr[i][j]
            else: break
        else: break
    else:
        if cnt >= 0: ans += 1

#세로방향 탐색
for j in range(n):
    cnt = 1
    prev = arr[0][j]
    for i in range(1, n):
        if arr[i][j] == prev:
            cnt += 1
        elif arr[i][j] == prev + 1: # 상승
            if cnt >= l:
                cnt = 1
                prev = arr[i][j]
            else: break
        elif arr[i][j] == prev - 1: # 하강
            if cnt >= 0:
                cnt = -l + 1
                prev = arr[i][j]
            else: break
        else: break
    else:
        if cnt >= 0: ans += 1

# output
print(ans)