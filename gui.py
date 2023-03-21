import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

import youtube_dl

window = tk.Tk()
window.geometry('620x125')
window.title('Download App')
window.resizable(False, False)

window.columnconfigure(0,weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

linkVideo = StringVar()
location = StringVar()

frame_top = Frame(window)
frame_bottom = Frame(window)

frame_top.grid(row=0,column=0, sticky='WENS')
frame_bottom.grid(row=1,column=0, sticky='WENS')


def GUI():
    lbURL = Label(
    frame_top, text='URL',pady=2 ,padx=5)
    lbURL.grid(row=1, column=0, pady=2 ,padx=20)
    txtURL = Entry(
    frame_top, width=66, textvariable=linkVideo)
    txtURL.grid(row=1, column=1)

    lbLocation = Label(
    frame_bottom, text='Location')
    lbLocation.grid(row=2, column=0, padx=7)
    txtLocation = Entry(
    frame_bottom, width=50, textvariable=location )
    txtLocation.grid(row=2, column=1, padx=5, pady=1)
    btnLocation = Button(
    frame_bottom, text = 'Location', width=11, relief=GROOVE,
    command=LocationFunc)
    btnLocation.grid(row=2, column=2, pady=1,padx=3)


    btnDownload = Button(
    frame_bottom, text = 'Download', width=11, relief=GROOVE,
    command=DownloadFunc)
    btnDownload.grid(row=3, column=1, pady=1,padx=3)

def LocationFunc():
    global down_Directory
    down_Directory = filedialog.askdirectory(
    initialdir ='Home', title = 'Save video')
    location.set(down_Directory)

def DownloadFunc():
    '''
        Cài đặt các option của chrome driver dẫn đến đường dẫn url
    '''
    global down_Directory

    # url = 'https://www.youtube.com/watch?v=T_ub4chD8cg'
    ydl_opts = {
        'outtmpl': f'{down_Directory}/%(title)s-%(id)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([linkVideo.get()])

def my_hook(d):
    if d['status'] == 'finished':
        messagebox.showinfo("SUCCESSFULLY",
                          "DOWNLOADED AND SAVED IN")

if __name__ == "__main__":
    linkVideo = StringVar()
    down_Directory = StringVar()
    GUI()
    window.mainloop()


