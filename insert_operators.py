import sys
sys.stdin = open('input.txt','r')

n = int(input())
lst_nums = list(map(int, input().split()))
lst_opr = list(map(int, input().split())) #덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수

min_val = sys.maxsize
max_val = -1 * sys.maxsize


def enum_opr(lst_opr):
    dict_opr = dict()
    for i, op in enumerate(lst_opr):
        dict_opr[i] = op
    return dict_opr


def cal(init_num, num, lst_opr):
    if lst_opr == 0:
        return init_num + num
    elif lst_opr == 1:
        return init_num - num
    elif lst_opr == 2:
        return init_num * num
    else:
        if init_num < 0:
            return -(-init_num // num)
        else: return init_num // num

lst_answer=[]
def solution(lst_nums, dict_opr):
    print(lst_nums, dict_opr)
    if len(lst_nums) == 1:
        print('end')
        lst_answer.append(lst_nums[0])
        return 0
    else:
        init_num = lst_nums.pop(0)
        tmp_num = lst_nums[0]

        #backtracking
        for idx, cnt_op in dict_opr.items():
            if cnt_op == 0: # == dict_opr[idx]
                continue
            else:
                num = cal(init_num, tmp_num, idx)
                dict_opr[idx] = dict_opr[idx] - 1 #계산 1회 수행했으므로

                if len(lst_nums) == 0:
                    lst_deliver = [num]
                else:
                    lst_deliver = [num] + lst_nums[1:]
                    print('num', num)
                    print('lst_nums[1:]', lst_nums[1:])
                    print('lst_deliver', lst_deliver)

                solution(lst_deliver, dict_opr)
                dict_opr[idx] = dict_opr[idx] + 1

dict_opr = enum_opr(lst_opr)
solution(lst_nums, dict_opr)
print(max(lst_answer))
print(min(lst_answer))

