import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# # 현재 재고가 바닥나는 시점 이전까지 받을 수 있는 라면 중 제일 많은 라면을 받는게 목표
# 1. 현재 재고의 상태에 따라 최고값을 받아야함
# 2. 제일 많은 값만 가져가면 된다.
#
# 1. 데이터를 넣을 때마다 최대값을 동적으로 변경
# 2. 최소/최대값을 바로 꺼낼 수 있는 자료구조
# --> Heap을 쓰면 되는구나

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    answer = 0
    current_day_index = 0
    max_heap =[]

    while stock < k:
        for date_index in range(current_day_index, len(dates)):
            if dates[date_index] <= stock:  # 10<4
                heapq.heappush(max_heap, -supplies[date_index])
            else:
                current_day_index = date_index
                break
        answer += 1
        stock += -heapq.heappop(max_heap)
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))