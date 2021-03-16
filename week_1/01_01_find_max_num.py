input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:
        for compare_num in array:
            print('for')
            if num < compare_num:
                print('if')
                break
        else: #for-else
            print('else')
            return num

    # 이 부분을 채워보세요!
    # return 1


result = find_max_num(input)
print(result)
