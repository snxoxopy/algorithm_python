input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    cnt_to_all_zero = 0
    cnt_to_all_one = 0
    if string[0] == '0':
        cnt_to_all_one += 1
    elif string[1] == '1':
        cnt_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            if string[i+1] == '0':
                cnt_to_all_one += 1
            if string[i+1] == '1':
                cnt_to_all_zero += 1
    print(cnt_to_all_zero, cnt_to_all_one)
    return min(cnt_to_all_zero, cnt_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)