import re
import urllib
import os
import sys
import urllib.request
import urllib.parse

urlopen = urllib.request.urlopen
encode = urllib.parse.urlencode
retrieve = urllib.request.urlretrieve
cleanup = urllib.request.urlcleanup()


def video_title(url):
    try:
        webpage = urlopen(url).read()
        title = str(webpage).split('<title>')[1].split('</title>')[0]
    except Exception:
        title = 'Youtube Song'

    return title


# download directly with a song name or link
def single_download(song_name: str = None):
    commands = ['youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ',
                'youtube-dl --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ']
    if "youtube.com/" not in song_name and "youtu.be/" not in song_name:
        # try to get the search result and exit upon error
        try:
            query_string = encode({"search_query": song_name})
            print(query_string)
            html_content = urlopen("https://www.youtube.com/results?" + query_string)
            print(html_content.read())
            search_results = re.findall(r'href="/watch\\?v=(.{11})', html_content.read().decode())
        except Exception as e:
            print('Network Error', repr(e))
            return None

        # make command that will be later executed
        command = f"{commands[0]} {search_results[0]}"

    else:  # For a link
        # make command that will be later executed
        command = f'{commands[1]} {song_name[song_name.find("=") + 1:]}'
        song_name = video_title(song_name)

    try:  # Try downloading song
        print('Downloading %s' % song_name)
        os.system(command)
    except Exception as e:
        print('Error downloading %s' % song_name, repr(e))
        return None


if __name__ == '__main__':
    url = 'https://youtu.be/DOn3y5FU7HQ'
    song = 'Theme of Laura'
    print(r'href="/watch\\?v=(.{11})')
    single_download(song)
