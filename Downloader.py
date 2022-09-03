
from tkinter import *
from pytube import YouTube
from tkinter import messagebox
import os

def ytsv():
    yt = YouTube(Url.get())

    messagebox.showinfo('Carregando', 'Iniciando download da musica \n Titulo: ' + yt.title)

    musica = yt.streams.get_audio_only()
    musica.download('Downloads')
    path_dir = 'Downloads'

    os.startfile(path_dir)


def ytcv():
    yt = YouTube(Url.get())

    messagebox.showinfo('Carregando','Iniciando download do video \n Titulo'+yt.title)

    video = yt.streams.get_highest_resolution()
    video.download('Downloads')
    path_dir = 'Downloads'

    os.startfile(path_dir)


tela = Tk()
tela.title("Download")
tela.resizable(0,0)
resolucao = Canvas(tela,width=350,height=200)
resolucao.pack(fill="both",expand=True)

tela.iconbitmap('download-icon-down-download-downloads-icon-1320196066868908267_49.ico')
bg = PhotoImage(file = "293537.png")

resolucao.create_image(0,0,image=bg,anchor="nw")

resolucao.create_text(40,88,text="Url do video: ",fill='white')






Url = Entry(tela,width=30)
entrada =resolucao.create_window(80,80,anchor='nw',window=Url)



botao = Button(tela, text="Download com video",command=ytcv)
botao2 = Button(tela, text="Download sem video",command=ytsv)


botao_resolucao=resolucao.create_window(15,140,anchor='nw',window=botao)
botao2_resolucao=resolucao.create_window(185,140,anchor='nw',window=botao2)



tela.mainloop()

