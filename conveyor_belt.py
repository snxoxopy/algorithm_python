import sys
from collections import deque
# input
sys.stdin = open('input.txt','r')
n, k = map(int, input().split())
#durab = [i for i in list(map(int, input().split()))]
durab = deque(list(map(int, input().split())))
# 로봇은 내려가면 0이기 때문에 올라간 자리만 고려한다.
robot = deque([0] * n)

# system
turn = 1
while True: # len(durab:내구도) >= k: break
    # 1. 벨트가 한칸 회전한다.
    durab.rotate(1)
    robot.rotate(1)
    # 마지막은 항상 내려가는 자리
    robot[-1] = 0
    #print('arr.rotate(1)', arr)

    # 2. 거꾸로 배열 탐색 (시작: 배열의 마지막 -1, 끝: 배열의 시작, -1만큼 이동)
    for i in range(-2, -n-1, -1):
        # 이동할 수 있는 조건은
        # 현재 칸에 로봇에 존재하고 robot[i] == 1
        # 다음 칸에 로봇이 없고 robot[i+1] == 0
        # 로봇이 없는 다음 칸의 durab > 0 이다.
        # i번째 로봇 존재 and  i+1 번째 로봇 없음 and 윗 벨트의 i+1번째 durab > 0
        if robot[i] == 1 and robot[i+1] == 0 and durab[i+1-n] > 0:
            robot[i] = 0
            # 로봇 이동
            robot[i+1] = 1
            # 내려가는 방향 배열에서 durability 감소
            durab[i+1-n] -= 1
            # 이동할 수 없다면 가만히 있는다.
    # 이동 후 마지막 칸에 있는 로봇은 내려간다.
    robot[-1] = 0

    #3. 올라가는 위치에 로봇이 없다면 추가한다.
    if robot[0] == 0 and durab[0] > 0:
        robot[0] = 1
        durab[0] -= 1

    #4. 내구도가 0인 칸의 개수가 k개 이상이라면 종료한다.
    if durab.count(0) >= k:
        break
    turn += 1

# output
print(turn)