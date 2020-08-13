from youtube_search import YoutubeSearch
import youtube_dl





musics = ['mic drop', '불타오르네', 'txt crown', 'bts boy with luv', 'in or out jens', '2002 anne marie']
for music in musics:
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': f'{music}.%(ext)s'
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    results = YoutubeSearch(music, max_results=1).to_dict()
    ydl.download(["https://www.youtube.com" + result['url_suffix'] for result in results])
