def solution(genres, plays):
    answer = list()

    play_music = dict()
    play_music_index = dict()
    play_music_sorted = dict()
    genre_sum = dict()
    genre_max_play = dict()

    for genre, play, index in zip(genres ,plays, range(len(genres))):    
        if genre not in play_music.keys():
            play_music[genre] = list()
            play_music_index[genre] = list()
        play_music[genre].append(play)
        play_music_index[genre].append(index)

    for genre in play_music.keys():
        play_music_sorted[genre] = sorted(play_music[genre], reverse=True)
        genre_sum[genre] = sum(play_music[genre])

    genre_sum = sorted(genre_sum.items(), key=lambda x : x[1], reverse=True)

    for genre, _ in genre_sum:
        if len(play_music[genre]) == 1 : 
            index = play_music[genre].index(play_music_sorted[genre][0])
            album_index = play_music_index[genre][index]
            answer.append(album_index)
        else : 
            for i in range(0, 2):
                index = play_music[genre].index(play_music_sorted[genre][i])
                play_music[genre][index] = -1
                album_index = play_music_index[genre][index]
                answer.append(album_index)

    return answer