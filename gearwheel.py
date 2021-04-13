import sys
from copy import deepcopy
from collections import deque

# input
sys.stdin = open("input.txt", "r")
gear = [list(map(int, input())) for _ in range(4)]
k = int(input())
info_gear = [list(map(int, input().split())) for _ in range(k)]


# system
def cnt_score(gear):
    score = 0
    for w in range(4):
        if gear[w][0] == 1:
            score += 2 ** w
    return score


def rot_gear(isrotate):
    for j in range(4):
        if isrotate[j][0]:
            # print('nwheel', j)
            # print('dir', isrotate[j][1])
            q_gear = deque(gear[j])
            q_gear.rotate(isrotate[j][1])
            gear[j] = list(q_gear)
    return gear

# main
for i in range(k):
    # print(k)
    isrotate = [[False for _ in range(4)] for _ in range(4)]
    nwheel = info_gear[i][0] - 1
    d = info_gear[i][1]
    isrotate[nwheel] = [True, d]

    # check_left
    for v in range(nwheel, -1, -1):
        if v - 1 == -1: break
        if gear[v][6] != gear[v - 1][2]:
            d *= -1
            isrotate[v - 1] = [True, d]
        else:
            break

    # check_right
    d = info_gear[i][1]
    for v in range(nwheel, 4):
        if v + 1 == 4: break
        if gear[v][2] != gear[v + 1][6]:
            d *= -1
            isrotate[v + 1] = [True, d]
        else:
            break

    gear = rot_gear(isrotate)


# output
print(cnt_score(gear))
