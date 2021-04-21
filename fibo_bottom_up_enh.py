def fib_optimized(n):
    # 코드를 작성하세요.
    cur, prev = 1, 0

    for i in range(1, n):
        cur, prev = cur + prev, cur

    # n번재 피보나치 수를 리턴한다.
    return cur


# 테스트
print(fib_optimized(3))
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))