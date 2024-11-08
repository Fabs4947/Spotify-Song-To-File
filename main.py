import subprocess
import time
import re as regex

file_path = 'current_song.txt'
last_song_title = ""

def get_spotify_window_title():
    """Fetch the title of the Spotify window if it is active."""
    try:
        result = subprocess.run(['tasklist', '/v', '/fo', 'csv'],capture_output=True, text=True,  check=True)
        lines =  result.stdout.splitlines()
        for line in lines:
            if 'Spotify.exe' in line:
                columns = regex.split(r'","', line)
                window_title = columns[-1].replace('"', '')
                return window_title
    except subprocess.CalledProcessError as error:
        print(f"Error scanning for Spotify window title: {error}")

def log_current_song():
    """Log the current Spotify song title to a file if Spotify is open."""
    global last_song_title
    song_title = get_spotify_window_title()
    if song_title !=last_song_title:
        print(f"Difference found between last checked and new song title. {last_song_title} (old) vs {song_title} (new)")
        if song_title in ["Spotify", "Spotify Premium"]:
            print("Playback is paused.")
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write("Playback is paused.")
        elif song_title:
            print(f"Current song title: {song_title}")
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write(song_title)
        else:
            print("Spotify window not found")
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write("Spotify window not found.")
        last_song_title = song_title
    

def start_tracking(time_inbetween_scans=2.5):
    print(f"Tracking songs. Interval: {time_inbetween_scans}")
    while True:
        log_current_song()
        time.sleep(time_inbetween_scans)

start_tracking()