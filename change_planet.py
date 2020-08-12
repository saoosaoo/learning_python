import os


for f in os.listdir():
    if f[:3] == '새파일':
        os.unlink(f)
