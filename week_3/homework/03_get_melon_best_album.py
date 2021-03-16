genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    n = len(genre_array)

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])

    print(genre_total_play_dict)
    print(genre_index_play_array_dict)

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_genre_play_array)

    result = []

    for genre, _value in sorted_genre_play_array:
        #[[1, 600], [4, 2500]]
        index_play_array = genre_index_play_array_dict[genre]
        sorted_index_play_array = sorted(index_play_array, key = lambda item: item[1], reverse=True)
        print(sorted_index_play_array)
        for i in range(len(sorted_index_play_array)):
            if i > 1:
                break
            result.append(sorted_index_play_array[i][0])
    return result

print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!