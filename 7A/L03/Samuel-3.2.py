song_dict = {
    'Bach': "Jesus, Joy of Man's Desiring",
    'beethoven': 'Symphony No. 9 - Ode to Joy',
    'mozart': 'The Marriage of Figaro'
}

song = input('what artist do you want to find? ')

try:
    print(song_dict[song])
except KeyError:
    print('that artist is not in the dictionary :(')

if song in song_dict:
    print(f'{song}:{song_dict.get(song)} :)')
else:
    print('that artist is not in the dictionary :(')

song = input('what artist do you want to find?')
if song in song_dict.values():
    for key in song_dict:
        if song_dict.get(key) == song:
            print(f'{key}:{poem}')

else:
    print('that artist is not in the dictionary :(')
