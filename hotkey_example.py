from pynput import keyboard
import youtube_dl
import pyperclip


def on_activate_h():
    youtube_url = pyperclip.paste()
    download_youtube_mp3(youtube_url)

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')     

def download_youtube_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': r'C:\\Users\Seungyeon\Desktop\\%(title)s.%(ext)s'
        }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([url])


# dictionary에서 key에 해당되는 단축키에 대해서 value 값으로서 단축키에 실행되는 함수를 등록해줍니다
with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': on_activate_h,
        '<ctrl>+<alt>+i': on_activate_i}) as h:
    h.join()

