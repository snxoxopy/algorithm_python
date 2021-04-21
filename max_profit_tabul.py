def max_profit(price_list, count):
    # 코드를 작성하세요.
    lst_profit = [0]

    for i in range(1, count + 1):
        print('i = %d' %i)
        if i < len(price_list):
            profit = price_list[i]
            print('     profit = price_list[%d] = %d' %(i, profit))
        else: profit = 0

        for j in range(1, i//2 + 1):
            print('     j = %d' %j)
            profit = max(profit, lst_profit[j] + lst_profit[i-j])
            print('         profit = max(profit, lst_profit[j->%d] + lst_profit[i-j->%d]) = %d' % (j, i-j, profit))

        lst_profit.append(profit)
        print(lst_profit)
    return lst_profit[count]




# 테스트
# print(max_profit([0, 100, 400, 800, 900, 1000], 5))
# # print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
# print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
