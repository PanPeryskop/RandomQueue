import customtkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import threading
import os
import configparser


playlist_count = 0


def add_random_track_to_queue():
    genres = [
        'acid house', 'acoustic blues', 'afrobeat', 'alternative metal', 'alternative rock', 'ambient', 'americana',
        'anarcho-punk',
        'anime', 'art pop', 'art rock', 'avant-garde jazz', 'bachata', 'ballad', 'baroque', 'bebop', 'big band',
        'black metal',
        'bluegrass', 'blues', 'blues rock', 'bolero', 'bossa nova', 'breakbeat', 'britpop', 'bubblegum pop', 'cajun',
        'calypso',
        'cantopop', 'chamber pop', 'chanson', 'chillout', 'choral', 'classic rock', 'classical', 'club', 'comedy',
        'contemporary jazz',
        'country', 'country blues', 'country rock', 'cowpunk', 'crossover thrash', 'crust punk', 'dance', 'dance-pop',
        'dancehall',
        'death metal', 'deathcore', 'delta blues', 'disco', 'doom metal', 'downtempo', 'drone', 'drum and bass', 'dub',
        'dubstep',
        'east coast hip hop', 'easy listening', 'electro', 'electro house', 'electronic', 'electronica', 'emo',
        'ethereal', 'eurodance',
        'europop', 'experimental', 'fado', 'flamenco', 'folk', 'folk rock', 'folktronica', 'freak folk', 'free jazz',
        'funk', 'funk metal',
        'funky house', 'fusion', 'future bass', 'g-funk', 'gabber', 'gangsta rap', 'garage rock', 'ghazal',
        'glam metal', 'glam rock',
        'glitch', 'gospel', 'gothic metal', 'gothic rock', 'grime', 'grindcore', 'groove metal', 'grunge', 'hard bop',
        'hard rock',
        'hardcore punk', 'hardstyle', 'heavy metal', 'hip hop', 'honky tonk', 'house', 'idm', 'indie folk', 'indie pop',
        'indie rock',
        'industrial', 'industrial metal', 'instrumental rock', 'irish folk', 'j-pop', 'j-rock', 'jazz', 'jazz fusion',
        'jazz rap',
        'jungle', 'k-pop', 'klezmer', 'krautrock', 'latin', 'latin pop', 'lo-fi', 'lounge', 'madchester', 'mandopop',
        'martial industrial',
        'math rock', 'melodic death metal', 'melodic hardcore', 'metal', 'metalcore', 'minimal', 'modal jazz',
        'modern blues',
        'modern classical', 'motown', 'mpb', 'neo soul', 'neoclassical', 'new age', 'new wave', 'no wave', 'noise',
        'noise pop',
        'noise rock', 'nu metal', 'nu jazz', 'oi', 'opera', 'orchestral', 'outlaw country', 'p-funk', 'pagode', 'pop',
        'pop punk',
        'pop rock', 'post-bop', 'post-grunge', 'post-hardcore', 'post-punk', 'post-rock', 'power metal', 'power pop',
        'prog',
        'progressive house', 'progressive metal', 'progressive rock', 'psychedelic', 'psychedelic rock', 'punk',
        'punk rock', 'r&b',
        'ragga', 'ragtime', 'rap', 'rap rock', 'reggae', 'reggaeton', 'rhythm and blues', 'rock', 'rock and roll',
        'rockabilly',
        'roots reggae', 'salsa', 'samba', 'screamo', 'shoegaze', 'singer-songwriter', 'ska', 'skate punk',
        'sludge metal', 'smooth jazz',
        'soca', 'soft rock', 'soul', 'southern rock', 'space rock', 'speed metal', 'stoner rock', 'surf rock', 'swing',
        'symphonic metal',
        'synth-pop', 'synthwave', 'tango', 'techno', 'thrash metal', 'trance', 'trap', 'trip hop', 'tropical house',
        'uk garage',
        'vaporwave', 'viking metal', 'vocal jazz', 'west coast hip hop', 'world', 'yacht rock', 'zouk', 'hyperpop', 'synthwave'
    ]
    available_genres = [
        'acid house', 'acoustic blues', 'afrobeat', 'alternative metal', 'alternative rock', 'ambient', 'americana',
        'anarcho-punk', 'anime', 'art pop', 'art rock', 'avant-garde jazz', 'bachata', 'ballad', 'baroque', 'bebop',
        'big band', 'black metal', 'bluegrass', 'blues', 'blues rock', 'bolero', 'bossa nova', 'breakbeat', 'britpop',
        'bubblegum pop', 'cajun', 'calypso', 'cantopop', 'chamber pop', 'chanson', 'chillout', 'choral', 'classic rock',
        'classical', 'club', 'comedy', 'contemporary jazz', 'country', 'country blues', 'country rock', 'cowpunk',
        'crossover thrash', 'crust punk', 'dance', 'dance-pop', 'dancehall', 'death metal', 'deathcore', 'delta blues',
        'disco', 'doom metal', 'downtempo', 'drone', 'drum and bass', 'dub', 'dubstep', 'east coast hip hop',
        'easy listening', 'electro', 'electro house', 'electronic', 'electronica', 'emo', 'ethereal', 'eurodance',
        'europop', 'experimental', 'fado', 'flamenco', 'folk', 'folk rock', 'folktronica', 'freak folk', 'free jazz',
        'funk', 'funk metal', 'funky house', 'fusion', 'future bass', 'g-funk', 'gabber', 'gangsta rap', 'garage rock',
        'ghazal', 'glam metal', 'glam rock', 'glitch', 'gospel', 'gothic metal', 'gothic rock', 'grime', 'grindcore',
        'groove metal', 'grunge', 'hard bop', 'hard rock', 'hardcore punk', 'hardstyle', 'heavy metal', 'hip hop',
        'honky tonk', 'house', 'idm', 'indie folk', 'indie pop', 'indie rock', 'industrial', 'industrial metal',
        'instrumental rock', 'irish folk', 'j-pop', 'j-rock', 'jazz', 'jazz fusion', 'jazz rap', 'jungle', 'k-pop',
        'klezmer', 'krautrock', 'latin', 'latin pop', 'lo-fi', 'lounge', 'madchester', 'mandopop', 'martial industrial',
        'math rock', 'melodic death metal', 'melodic hardcore', 'metal', 'metalcore', 'minimal', 'modal jazz',
        'modern blues', 'modern classical', 'motown', 'mpb', 'neo soul', 'neoclassical', 'new age', 'new wave', 'no wave',
        'noise', 'noise pop', 'noise rock', 'nu metal', 'nu jazz', 'oi', 'opera', 'orchestral', 'outlaw country',
        'p-funk', 'pagode', 'pop', 'pop punk', 'pop rock', 'post-bop', 'post-grunge', 'post-hardcore', 'post-punk',
        'post-rock', 'power metal', 'power pop', 'prog', 'progressive house', 'progressive metal', 'progressive rock',
        'psychedelic', 'psychedelic rock', 'punk', 'punk rock', 'r&b', 'ragga', 'ragtime', 'rap', 'rap rock', 'reggae',
        'reggaeton', 'rhythm and blues', 'rock', 'rock and roll', 'rockabilly', 'roots reggae', 'salsa', 'samba',
        'screamo', 'shoegaze', 'singer-songwriter', 'ska', 'skate punk', 'sludge metal', 'smooth jazz', 'soca',
        'soft rock', 'soul', 'southern rock', 'space rock', 'speed metal', 'stoner rock', 'surf rock', 'swing',
        'symphonic metal', 'synth-pop', 'synthwave', 'tango', 'techno', 'thrash metal', 'trance', 'trap', 'trip hop',
        'tropical house', 'uk garage', 'vaporwave', 'viking metal', 'vocal jazz', 'west coast hip hop', 'world',
        'yacht rock', 'zouk', 'hyperpop', 'synthwave'
    ]
    genres.extend(available_genres)
    genres.extend(get_genres())
    random_genre = random.choice(genres)
    results = sp.search(q=f'genre:"{random_genre}"', type='track', limit=50)
    tracks = results['tracks']['items']

    if not tracks:
        print("No tracks found.")
        return

    random_track = random.choice(tracks)
    track_uri = random_track['uri']
    sp.add_to_queue(uri=track_uri)


def update_slider(event, slider):
    value = event.widget.get()
    if value.isdigit():
        slider.set(int(value))


def slider_activity(value, user_input):
    user_input.delete(0, 'end')
    user_input.insert(0, int(value))


def end_program():
    end_label = tk.CTkLabel(app, text="Tracks added successfully!", font=("Roboto", 20, "bold"), text_color="green")
    end_label.place(relx=0.5, rely=0.5, anchor='center')
    app.after(5000, app.quit)


def check_thread(thread, wait_label):
    if thread.is_alive():
        app.after(100, check_thread, thread, wait_label)
    else:
        wait_label.destroy()
        end_program()


def add_queue():
    for i in range(playlist_count):
        add_random_track_to_queue()


def process_user_input(input, user_input, input_frame):
    global playlist_count
    if input.isdigit() and int(input) > 0:
        playlist_count = int(input)
        user_input.destroy()
        for widget in input_frame.winfo_children():
            widget.destroy()

        wait_label = tk.CTkLabel(app, text="Adding tracks to queue...", font=("Roboto", 20, "bold"), text_color="cyan")
        wait_label.place(relx=0.5, rely=0.5, anchor='center')

        thread = threading.Thread(target=add_queue)  # Remove the parentheses after add_queue
        thread.start()
        check_thread(thread, wait_label)
    else:
        error_label = tk.CTkLabel(app, text="Please enter a number.")
        error_label.pack()
        app.after(5000, error_label.destroy)


def get_genres():
    genres = sp.recommendation_genre_seeds()
    return genres['genres']


def get_user_input(input_frame):
    input_frame.pack(fill=tk.BOTH, expand=True)
    s_label = tk.CTkLabel(master=input_frame, text="How many tracks do you want to add", font=("Roboto", 18, "bold"))
    s_label.pack(pady=(30, 0), anchor='s')
    user_input = tk.CTkEntry(input_frame)
    user_input.pack(pady=15)
    user_input.bind('<KeyRelease>', lambda event: update_slider(event, slider))
    slider = tk.CTkSlider(input_frame, from_=1, to=100, number_of_steps=99, command=lambda value: slider_activity(value, user_input))
    slider.pack(pady=15)
    submit_button = tk.CTkButton(input_frame, text="Submit", command=lambda: process_user_input(user_input.get(), user_input, input_frame))
    submit_button.place(relx=0.5, rely=0.5, anchor='center')
    app.mainloop()


def get_user_input_config():
    input_frame = tk.CTkFrame(app)
    input_frame.pack(fill=tk.BOTH, expand=True)

    client_id_label = tk.CTkLabel(input_frame, text="Enter your client_id:", font=("Roboto", 16, "bold"), text_color="white")
    client_id_label.pack(pady=(40, 0))
    client_id_entry = tk.CTkEntry(input_frame)
    client_id_entry.pack(pady=5)

    client_secret_label = tk.CTkLabel(input_frame, text="Enter your client_secret:", font=("Roboto", 16, "bold"), text_color="white")
    client_secret_label.pack(pady=(30, 0))
    client_secret_entry = tk.CTkEntry(input_frame)
    client_secret_entry.pack(pady=5)

    redirect_uri_label = tk.CTkLabel(input_frame, text="Enter your redirect_uri:", font=("Roboto", 16, "bold"), text_color="white")
    redirect_uri_label.pack(pady=(30, 0))
    redirect_uri_entry = tk.CTkEntry(input_frame)
    redirect_uri_entry.pack(pady=5)

    submit_button = tk.CTkButton(input_frame, text="Submit", font=("Roboto", 10), text_color="white", command=lambda: process_user_input_config(client_id_entry.get(), client_secret_entry.get(), redirect_uri_entry.get(), input_frame))
    submit_button.place(relx=0.5, rely=0.9, anchor='s')
    app.mainloop()


def process_user_input_config(client_id, client_secret, redirect_uri, input_frame):
    config['SPOTIFY'] = {'client_id': client_id, 'client_secret': client_secret, 'redirect_uri': redirect_uri}

    with open(config_file, 'w') as configfile:
        config.write(configfile)

    input_frame.destroy()
    app.quit()


def end_all():
    app.quit()
    quit()


app = tk.CTk()
app.title("RandomQueue")
app.geometry("420x600")
app.protocol("WM_DELETE_WINDOW", end_all)

config_file = 'config.sg'
config = configparser.ConfigParser()

if not os.path.exists(config_file):
    get_user_input_config()
    config.read(config_file)
    client_id = config.get('SPOTIFY', 'client_id')
    client_secret = config.get('SPOTIFY', 'client_secret')
    redirect_uri = config.get('SPOTIFY', 'redirect_uri')
else:
    config.read(config_file)
    client_id = config.get('SPOTIFY', 'client_id')
    client_secret = config.get('SPOTIFY', 'client_secret')
    redirect_uri = config.get('SPOTIFY', 'redirect_uri')

scope = 'playlist-read-private user-modify-playback-state playlist-modify-public playlist-modify-private user-top-read'
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

input_frame = tk.CTkFrame(app)
get_user_input(input_frame)

