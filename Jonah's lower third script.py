def play_current_song(songs, current_song_index):
    print("Now playing:", songs[current_song_index])
    update_current_song_file(songs[current_song_index])

def next_song(songs, current_song_index):
    current_song_index = (current_song_index + 1) % len(songs)
    play_current_song(songs, current_song_index)
    return current_song_index

def previous_song(songs, current_song_index):
    current_song_index = (current_song_index - 1) % len(songs)
    play_current_song(songs, current_song_index)
    return current_song_index

def update_current_song_file(song_name):
    with open("current_song.txt", "w") as f:
        f.write(song_name)

def read_song_list_from_file(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

songs = read_song_list_from_file("songs.txt")

current_song_index = 0

play_current_song(songs, current_song_index)

while True:
    user_input = input("Enter 'n' for next song, 'p' for previous song, or 'q' to quit: ").lower()
    if user_input == 'n':
        current_song_index = next_song(songs, current_song_index)
    elif user_input == 'p':
        current_song_index = previous_song(songs, current_song_index)
    elif user_input == 'q':
        print("Quitting the music player.")
        break
    else:
        print("Invalid input. Please enter 'n', 'p', or 'q'.")
