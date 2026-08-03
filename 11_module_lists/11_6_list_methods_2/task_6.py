num, songs = int(input()), []
for _ in range(num):
    songs.append(input())

songs.sort()
print(*songs, sep='\n')
