import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar
from logic import * 
from tkinter import messagebox
import time

window = tk.Tk()
window.geometry('620x180')
window.title('Download App')
window.resizable(False, False)

window.columnconfigure(0,weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2,weight=1)

linkVideo = StringVar()
location = StringVar()

frame_top=Frame(window,bg='#B3E6E8')
frame_end=Frame(window,bg='#B3E6E8')
frame_bottom=Frame(window,bg='#B3E6E8')

frame_top.pack(fill=X)
frame_bottom.pack(fill=X)
frame_end.pack(fill=X)

pd = Progressbar (
        frame_end,
        orient='horizontal',
        mode="determinate",
        length=600
)
pd.pack(fill=BOTH,padx=5, pady=5)

def GUI():
    lbURL = Label(frame_top, text='Video URL:', width=10,bg='#B3E6E8')
    lbURL.pack(side=LEFT, anchor=N,padx=5, pady=5)

    global txtURL
    txtURL = Entry(frame_top, textvariable=linkVideo)
    txtURL.pack(fill=BOTH, expand=True,padx=5, pady=5)

    lbLocation = Label(frame_bottom, text='Save to:',width=10,bg='#B3E6E8')
    lbLocation.pack(side=LEFT, anchor=N,padx=5, pady=5)
    global txtLocation
    txtLocation = Entry(frame_bottom, textvariable=location, state=DISABLED,disabledbackground='#FFFFFF')
    txtLocation.pack(fill=BOTH, expand=True,padx=5, pady=5)

    btnLocation = Button(frame_end, text = 'Browser',relief=RAISED,bg='#B3E6E8',
    command=lambda: LocationFunc(location))
    btnLocation.pack(fill=BOTH,padx=5, pady=5)

    btnDownload = Button(
    frame_end, text = 'Download', width=72, relief=RAISED,bg='#B3E6E8',
    command=lambda: DownloadFunc(linkVideo, location,my_hook))
    btnDownload.pack(fill=BOTH,padx=5, pady=5)

def my_hook(d):
    if d['status'] == 'finished':
        messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN")
        pd['value'] = 0
    #txtURL.set("")
    #txtLocation.set("")
       
    if d['status'] == 'downloading':
        pd['value'] += 20
        window.update_idletasks()
        time.sleep(0.5)

if __name__ == "__main__":
    linkVideo = StringVar()
    GUI()
    window.mainloop()


