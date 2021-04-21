import sys
sys.stdin = open("input.txt",'r')

# input
# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
print(dp)


# system
for i in range(1, n):
    for j in range(i + 1):
        print('dp[i:%d][j:%d] = %d' %(i, j, dp[i][j]))
        if j == 0:
            print(' if j == 0: up_left = 0')
            up_left = 0
        else:
            print(' else: up_left = dp[i-1][j-1] = %d' %dp[i-1][j-1])
            up_left = dp[i - 1][j - 1]
        if j == i:
            print(' if j == i: up = 0')
            up = 0
        else:
            print(' else: up = dp[i-1][j] = %d' %dp[i-1][j])
            up = dp[i - 1][j]
        dp[i][j] = dp[i][j] + max(up_left, up)
        print(' dp[i][j] + max(up_left, up) = %d' %dp[i][j])
    print(dp)

# output
# 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
print(max(dp[n-1]))