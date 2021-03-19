def triangle(n):
    res = [[0] * n for _ in range(n)]
    ans = []
    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
                #print('i % 3 == 0')
            elif i % 3 == 1:
                y += 1
                #print('i % 3 == 1')
            elif i % 3 == 2:
                x -= 1
                y -= 1
                #print('i % 3 == 2')
            res[x][y] = num
            num += 1
    #print(res)
    for i in res:
        print(i)
        for j in i:
            print(j)
            if j != 0:
                ans.append(j)
    return ans

print(triangle(4))