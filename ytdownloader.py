import yt_dlp
import os
from typing import List


class color:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'


# clear terminal
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


ffmpeg_path = f"{os.path.abspath('..')}\\ytdl"
download_path = f"{os.path.abspath('..')}\\music"
''' youtube-dl options '''
yt_dlp_options = {
        # PERMANENT options
        'quiet': True,
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_path,
        'keepvideo': False,
        'outtmpl': f'{download_path}/%(title)s.webm',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }],

        # OPTIONAL options
        'noplaylist': True,
        'noprogress': True,
    }

''' Printing on terminal '''


def print_status(status, num):
    clear()
    print(
            f"{color.ERROR}yt{color.WARNING}mp3-dl {color.OKGREEN}v3.0 {color.OKCYAN}~poseidon-code{color.ENDC}\n"
            f"{color.ERROR}|{color.ENDC} URLs                       : {num}\n"
            f"{color.ERROR}|{color.ENDC} Download Directory         : {download_path}"
    )
    print()
    [print(item) for item in status]


def download_mp3(urls):
    status: List[str] = []
    title = ''
    for url in urls:
        status.append(url)
        with yt_dlp.YoutubeDL(yt_dlp_options) as mp3:
            info = mp3.extract_info(url, download=False)
            title = (info.get('title', None))

            status[urls.index(url)] = f"{color.WARNING}[downloading]{color.ENDC}\t {title}"
            print_status(status, len(urls))

            mp3.download([url])

            status[urls.index(url)] = f"{color.OKGREEN}[finished]{color.ENDC}\t {title}"
            print_status(status, len(urls))

    os.rename(f"{download_path}\\{title}.mp3", f"{download_path}\\{title.lower()}.mp3")


if __name__ == '__main__':
    print(os.path.abspath('..'))
    #download_mp3(['https://youtu.be/td3P1-cfZ4E'])
