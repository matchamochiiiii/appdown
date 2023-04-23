import tkinter as tk
from tkinter import *
from tkinter import  filedialog, messagebox

import youtube_dl


def LocationFunc(location):
    down_Directory = filedialog.askdirectory(
    initialdir ='Home', title = 'Save video')
    location.set(down_Directory)

def DownloadFunc(linkVideo,location, my_hook):
    if linkVideo.get() != '':
        ydl_opts = {
            'outtmpl':f'{location.get()}/%(title)s-%(id)s.%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/best',
            'progress_hooks': [my_hook],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([linkVideo.get()])
            except:
                messagebox.showinfo("Error", "Link video invalid")
            
    else:
        messagebox.showinfo("Error", "Link video should not be EMPTY")



