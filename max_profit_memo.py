def max_profit_memo(price_list, count, cache):
    # 코드를 작성하세요.
    # Base case는 n이 0이거나 1일 때입니다.
    # 새꼼달꼼 0개 혹은 1개를 팔려고 하면, 부분 문제로 나눌 필요 없이 바로 주어진 가격을 리턴하면 됩니다.
    if count < 2:
        cache[count] = price_list[count]
        print('if count < 2: cache[count]', count, cache[count])
        return price_list[count]
    # Recursive case에는 두 가지 경우가 있습니다.
    # 이미 계산한 값이면 cache에 저장된 값을 리턴한다
    # 새꼼달꼼 i개를 팔아서 가능한 최대 수익을 이미 계산한 경우, 즉 cache[i]가 존재하는 경우
    if count in cache:
        print('if count in cache', cache[count])
        return cache[count]
    # 새꼼달꼼 i개를 팔아서 가능한 최대 수익을 아직 계산하지 않은 경우, 즉 cache[i]가 존재하지 않는 경우
    if count < len(price_list):
        print('if count < len(price_list): profit', price_list[count])
        profit = price_list[count]
    else: profit = 0

    # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
    for i in range(1, count // 2 + 1):
        print('for', i, count - i)
        print('profit1', profit)
        profit = max(profit, max_profit_memo(price_list, i, cache)
                     + max_profit_memo(price_list, count - i, cache))
        print('profit2', profit)
    # 계산된 최대 수익을 cache에 저장
    cache[count] = profit
    print(cache)

    return profit



def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
# print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
# print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
