def fibo_tab(n):
    # 계산된 피보나치 수를 담을 LIST
    lst_fibo = [0, 1, 1]

    for i in range(3, n+1):
        lst_fibo.append(lst_fibo[i - 1] + lst_fibo[i - 2])

    return lst_fibo[n]


# 테스트
print(fibo_tab(10))
print(fibo_tab(56))
print(fibo_tab(132))