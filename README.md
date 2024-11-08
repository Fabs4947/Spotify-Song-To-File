# Spotify Song Tracker for OBS

This project is a simple Python script designed to capture the current song playing on Spotify and log it into a text file. This file can then be used as an overlay in [OBS Studio](https://obsproject.com/) to display what song you're listening to live on your stream.

## Features

- **Real-Time Song Tracking**: Captures the currently playing Spotify song and updates the file whenever the song changes.
- **OBS Integration**: Outputs the song title to a `.txt` file that can be used as a text source in OBS for your live stream.
- **Playback Detection**: Identifies when Spotify playback is paused or if the Spotify window isn’t open, and displays appropriate messages.

## Use Case

The primary use case is to provide streamers with a way to show their viewers what song they're currently listening to, directly on their OBS overlay. This adds a fun, interactive element to streams and lets viewers connect with your music choices.

## Requirements

- **Python 3.7+**
- **Spotify Desktop Application** (Windows only)
- OBS Studio/Streaming Software of your choice.

## Installation

 Clone the repository:

   ``` bash
   git clone https://github.com/Fabs4947/spotify-song-tracker-obs.git
   cd spotify-song-tracker-obs 
   ```

## Configuration

### Setting up in OBS

1. Open OBS Studio.
2. Add a new **Text (GDI+)** source.
3. In **Text Source** properties, select **Read from file**.
4. Select ```current_song.txt``` or the changed file name.
5. Customize the source as you desire.

### Running it via .bat file

Due to currently unresolved issues from running the script directly, it is recommended to run it using a .bat file.

```bat
@echo off
cd **location of the file**
python main.py
pause
```

Like this, you can run it from any location on your PC.

### Settings

#### Polling Interval

You can update the polling interval by modifying the ```start_tracking()``` function.

``` python
start_tracking(time_inbetween_scans=2.5) 
```

By changing the value of the ```time_inbetween_scans``` variable, you can change the delay, in seconds.

#### File Path

By default, the output file is ```current_song.txt``` in the same directory. You can change this by modifying the ```file_path``` variable at the top of ```main.py```.

## Limitations

- Windows Only: As this script uses the ```tasklist``` command, it is only available on Windows. Alternatives are under development.
- Spotify Desktop App: Spotify must be open on the desktop, as the script checks for the process of the executable file. It does not work with the web player.

### Contact me

I'm available for contact under the discord username ```fabslxxv```, my discord ID is ```306800551633354752```.

## Donations

If you find this project useful and would like to support its development, as well as me, feel free to make a donation. Your support is greatly appreciated!

[Donate via PayPal](https://www.paypal.me/fabslxxv)
