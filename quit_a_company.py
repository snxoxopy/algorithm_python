import sys
sys.stdin = open('input.txt','r')
n = int(input())
t = []
p = []
dp = [0] * (n + 1)
max_val = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i
    print('time = t[%d]->%d + %d' %(i, t[i], i))
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_val)
        print(' if time(%d) <= n(%d):' %(time, n))
        print(' dp[%d] = max(p[%d] -> %d + dp[%d] -> %d, max_val->%d)' %(i, i, p[i], time, dp[time], max_val))
        max_val = dp[i]
        print(' max_val = ',max_val)
    else:
        dp[i] = max_val
        print(' else: -> time > n')
        print(' dp[%d] = max_val -> %d' %(i, max_val))

print(max_val)