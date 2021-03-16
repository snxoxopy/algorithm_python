"""
16/03/2021
https://www.acmicpc.net/problem/1748
Time limit : 150ms
Input: 1 <= n <= 100,000,000
O(NlogN) -> N 반복문, logN str 연산
"""
print('hello')

input = 120

def _cnt_the_len_of_num(n):
    ret, l = 0, len(str(n))
    for i in range(1, l): ret += i * (10 ** i - 10 ** (i - 1))
    ret += l * (n - 10 ** (l - 1) + 1)
    return print(ret)


_cnt_the_len_of_num(input)

"""
case1) 한 자리 9개
case2) 두 자리 90개
case3) 세 자리 21개
ans = case1) + case2) + case3)
    = 9      + 2*90   + 3*21
"""