seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}

def fibo_dynamic_programming(n, fibo_memo):
    # 구현해보세요!
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    cur_idx = 0
    for fixed_seat in fixed_seat_array:
        fix_seat_idx = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fix_seat_idx - cur_idx, memo)
        #곱연산
        all_ways *= count_of_ways
        cur_idx = fix_seat_idx + 1

    all_ways *= fibo_dynamic_programming(total_count - cur_idx, memo)
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))