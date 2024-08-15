# Modules and packages
import os
import yt_dlp

# Directories and path
AUDIO_DOWNLOAD_DIR = "" # choose a folder to save downloaded audio 

if not AUDIO_DOWNLOAD_DIR:
    raise ValueError("Please set AUDIO_DOWNLOAD_DIR in the script.")

ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'ffmpeg-2024-08-07-git-94165d1b79-essentials_build', 'bin', 'ffmpeg.exe')

# Audio download function
def YoutubeAudioDownload(video_url, artist):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{AUDIO_DOWNLOAD_DIR}/{artist} - %(title)s.%(ext)s' if artist else f'{AUDIO_DOWNLOAD_DIR}/%(title)s.%(ext)s',
            'nocheckcertificate': True,  
            'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
            {'key': 'EmbedThumbnail'},
            {'key': 'FFmpegMetadata'}
            ],
            'writethumbnail': True,
            'ffmpeg_location': ffmpeg_path
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print(f"Downloaded to {AUDIO_DOWNLOAD_DIR}")
    except Exception as e:
        print(f"Failed to download audio: {e}")

# User input
video_url = input("Enter a YouTube URL to download audio: ")
artist = input("Enter the name of the artist/creator, or skip this step: ")

# Function call 
YoutubeAudioDownload(video_url, artist)

