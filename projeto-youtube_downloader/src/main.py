from pytube import YouTube
from pytube import Search
from pytube import Playlist
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *


# link =  input("digite seu link:")
# link = "https://www.youtube.com/watch?v=tEcs_Hf6r_E"
# print(link)

def isYoutubePlaylist():
    if link.get().__contains__("list="):
        print("playlist detectado")
        return True
    else:
        print("link unico detectado")
        return False


def isYoutubeLink():
    if link.get().__contains__("https://www.youtube.com/"):
        return True
    else:
        return False


main = Tk()
main.title('VIDEO DOWNLOADER')


def youtube_link():
    blank.delete(0, END)
    print(link.get())
    if(not isYoutubeLink()):
        blank.insert(0,"link não válido")
    else:

        if(isYoutubePlaylist()):
            print("trabalhando com playlist")
            blank.insert(0, "playlist preparada para download")
            yt = YouTube(link.get())
            print(yt.streams.filter(progressive=True, file_extension='mp4'))
            title.insert(0, "PLAYLIST: " + yt.title)

        else:
            print("trabalhando o link único")
            blank.insert(0, "video preparado para download")
            yt = YouTube(link.get())
            print(yt.streams.filter(progressive=True, file_extension='mp4'))
            title.insert(0,yt.title)


def download():
    blank.delete(0, END)
    blank.insert(0, "fazendo o download... aguarde")
    print(formatchosen.current())


main.geometry('900x300')
Label(main, text="Youtube Link: ").grid(row=0)
Label(main, text="Video Title: ").grid(row=1)
Label(main, text="Output:").grid(row=2)

link = Entry(main)
title = Entry(main)
blank = Entry(main)


formatchosen = ttk.Combobox(main, width=27)

# Adding combobox drop down list
formatchosen['values'] = (' MP4 360p',
                          ' MP4 720p',
                          ' MP4 1080p',)

formatchosen.grid(column=1, row=5)
formatchosen.current()

link.grid(row=0, column=1)
title.grid(row=1, column=1)
blank.grid(row=2, column=1)

Button(main, text='Quit', command=main.destroy).grid(row=10, column=1, sticky=W)
Button(main, text='Procurar', command=youtube_link).grid(row=0, column=3, sticky=W, )
Button(main, text='Download', command=download).grid(row=3, column=1, sticky=W)


mainloop()
