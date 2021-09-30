from pytube import YouTube
from pytube import Search
from pytube import Playlist
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import os


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
            print(type(yt.streams.filter(file_extension='mp4')))
            print(yt.streams.get_by_resolution(resolution="1080p"))
            print(yt.streams.get_by_resolution(resolution="720p"))
            print(yt.streams.get_by_resolution(resolution="480p"))
            print(yt.streams.get_by_resolution(resolution="360p"))
            print(yt.streams.get_by_resolution(resolution="240p"))
            print(yt.streams.get_by_resolution(resolution="144p"))
            arrayy = [yt.streams.get_by_resolution(resolution="1080p"),
                      yt.streams.get_by_resolution(resolution="720p"),
                      yt.streams.get_by_resolution(resolution="480p"),
                      yt.streams.get_by_resolution(resolution="360p"),
                      yt.streams.get_by_resolution(resolution="240p"),
                      yt.streams.get_by_resolution(resolution="144p"),
                      ]
            exist = []
            for x in arrayy:
                if(x != None):
                    exist.append(x.resolution)

            print("arrayy criado com as seguintes resolucoes: ", exist)
            formatchosen['values'] = tuple(exist)
            print(formatchosen.get())

            title.insert(0,yt.title)




def download():
    blank.delete(0, END)
    blank.insert(0, "Download...")
    print(formatchosen.current())
    formatchosen.grid(column=0, row=6)
    print(formatchosen.get())
    os.chmod(os.path.dirname(os.path.abspath(__file__)), 0o777)
    x = os.path.dirname(os.path.abspath(__file__))
    print(x)

    try:
        os.makedirs(os.path.dirname(os.path.abspath(__file__)) + '/downloads', mode=0o777)
    except FileExistsError:
        print("/downloads already make")
    yt = YouTube(link.get())
    blank.insert(END, " Link ok...")
    if(formatchosen.get() == -1):
        print("resolução não selecionada")
    else:
        blank.delete(0, END)
        blank.insert(0, " Resolução selecionada: " + str(formatchosen.current()))
        blank.insert(END, " Aguarde... ")
        print(yt.streams.get_by_resolution(resolution=formatchosen.current()))
        stream = yt.streams.get_by_resolution(resolution=formatchosen.current())
        print(stream.itag)
        file = yt.streams.get_by_itag(stream.itag)
        file.download(output_path=os.path.dirname(os.path.abspath(__file__)) + '/downloads')
        blank.delete(0, END)
        blank.insert(0, "Download concluído!")





main.geometry('500x300')
Label(main, text="Youtube Link: ").grid(row=0)
Label(main, text="Video Title: ").grid(row=1)
Label(main, text="Output:").grid(row=2)

link = Entry(main)
title = Entry(main)
blank = Entry(main)


formatchosen = ttk.Combobox(main, width=13)

# Adding combobox drop down list
formatchosen['values'] = ("procure um link primeiro")

formatchosen.grid(column=0, row=3)
formatchosen.current()

link.grid(row=0, column=1)
title.grid(row=1, column=1)
blank.grid(row=2, column=1)

Button(main, text='Sair', command=main.destroy).grid(row=10, column=3, sticky=W)
Button(main, text='Procurar', command=youtube_link).grid(row=0, column=3, sticky=W, )
Button(main, text='Download', command=download).grid(row=3, column=1, sticky=W)


mainloop()
