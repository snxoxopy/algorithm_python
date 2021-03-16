input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_len_arr = []
    for split_size in range(1, n//2 +1):
        """
        splited = [] 
        for i in range(0, n, split_size):
            splited.append(string[i: i+split_size])
        """
        splited = [
            string[i: i+split_size] for i in range(0, n, split_size)
        ]
        cnt = 1
        compressed = ""
        for j in range(1, len(splited)):
            prev, cur = splited[j-1], splited[j]
            if prev == cur:
                cnt += 1
            else:
                if cnt > 1:
                    compressed += (str(cnt) + prev)
                else:
                    compressed += prev
                cnt = 1
        if cnt > 1:
            compressed += (str(cnt) + splited[-1])
        else:
            compressed += splited[-1]
        #print(compressed)
        compression_len_arr.append(len(compressed))
    return min(compression_len_arr)


print(string_compression(input))  # 14 가 출력되어야 합니다!