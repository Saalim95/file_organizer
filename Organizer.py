import os
import shutil

form = lambda x: x[-3:]

d={
    'mp3': 'Music',
    'exe': 'Programs',
    'pdf': 'Documents',
    'mp4': 'Video',
    'zip': 'Compressed',
    'jpg': 'Images',
    }

user = os.getenv('username')
path='c://Users/PiedPiper/Downloads/'
os.chdir(path)
files = os.listdir()
for file in files:
    try:                    # for files not folder
        if file[-4]=='.':
            f = form(file)
            if f in d:
                foldername=d[f]
            else:
                foldername=f+' files'
            if foldername in os.listdir():
                shutil.move(file, foldername)
            else:
                os.mkdir(foldername)
                shutil.move(file, foldername)

    except IndexError:
        pass
print('files organised')
