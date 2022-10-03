# input
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다.
# 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
n, m = map(int, input().split())
arr = list(map(int, input().split()))


"""
others
https://www.acmicpc.net/source/20955937

def get_maxnum(n, m, lst_nums):
    nums = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                n_sum = lst_nums[i] + lst_nums[j] + lst_nums[k]
                if n_sum <= m:
                    nums.add(n_sum)
                    break
    return max(nums)

print(get_maxnum(n, m, sorted(arr, reverse=True)))
"""
# https://www.acmicpc.net/submit/2798/50015993

n_max = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] > m:
                continue
            else:
                n_max = max(arr[i] + arr[j] + arr[k], n_max)

print(n_max)
