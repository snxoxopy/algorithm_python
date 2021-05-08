# https://programmers.co.kr/learn/courses/30/lessons/67256

# 엄지 손가락 상하좌우 4가지 방향
# 맨 처음 왼손 엄지손가락은 *10 키패드에 오른손 엄지손가락은 #12
# 왼 147
# 오 369
# 2580
# 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

def solution(numbers, hand):
    answer = ''
    pos_r = [10]
    pos_l = [12]
    for number in numbers:
        if number == 0: number = 11
        if number % 3 == 1 and number <= 7: # left
            answer += "L"
            pos_l.append(number)
        elif number % 3 == 0 and number <= 9: #right
            answer += "R"
            pos_r.append(number)
        else:
            row_cur = (number - 1) // 3
            col_cur = (number - 1) % 3
            row_prev = (pos_l[-1] - 1) // 3
            col_prev = (pos_l[-1] - 1) % 3
            dist_l = abs(row_cur - row_prev) + abs(col_cur - col_prev)

            row_prev = (pos_r[-1] - 1) // 3
            col_prev = (pos_r[-1] - 1) % 3
            dist_r = abs(row_cur - row_prev) + abs(col_cur - col_prev)

            print('number, dist_l, dist_r', number, dist_l, dist_r)

            if dist_l < dist_r:
                answer += "L"
                pos_l.append(number)
            elif dist_r < dist_l:
                answer += "R"
                pos_r.append(number)
            else:
                if hand == "left":
                    answer += "L"
                    pos_l.append(number)
                else:
                    answer += "R"
                    pos_r.append(number)

    return answer

nums, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
print(solution(nums, hand))