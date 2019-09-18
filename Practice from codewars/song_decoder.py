def song_decoder(song):
    song = song.replace('WUB', ' ')
    song = ' '.join(song.split())
    song = song.strip()
    return song


print(song_decoder('WUBBABCWUBBWUB'))
