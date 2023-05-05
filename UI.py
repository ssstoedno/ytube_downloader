#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import StringVar, filedialog,messagebox
import urllib.request as urlreq
from pytube import YouTube



global path,url,download_videoaudio_button,download_audio_button,download_video_button
count=0

#window
window=tk.Tk()
window.configure(background="brown")
window.resizable(width=False,height=False)
window.geometry("500x500")
window.title("ss01 youtube downloader")


#topframe
topframe=tk.Frame(window,background="brown")
topframe.pack()

label=tk.Label(topframe,text="YOU_tube video URL:",font=('TimesNewRoman',15,'bold italic'),background="brown",fg="white")
label.pack(side="top", pady=("50","10"))


def download_audio():
    try:
        path[0]
    except:
        messagebox.showerror("Error", "No download location")
    else:
        audio = YouTube(link.get()).streams.filter(only_audio=True).first()
        audio.download(path)
        anametwp=f"{path}/{audio.default_filename.removesuffix('.mp4')}_audioonly.mp3"
        os.rename(path+"/"+audio.default_filename,anametwp)
def download_video():
    try:
        path[0]
    except:
        messagebox.showerror("Error", "No download location")
    else:
        videowoaudio = YouTube(link.get()).streams.filter(only_video=True).first()
        videowoaudio.download(path)
        aname = f"{path}/{videowoaudio.default_filename.removesuffix('.mp4')}_videowoaudio.mp4"
        os.rename(path+"/"+videowoaudio.default_filename, aname)



def download_videaudio():
    try:
        path[0]
    except:
        messagebox.showerror("Error", "No download location")
    else:
        video = url.streams.filter(progressive=True).get_highest_resolution()
        video.download(path)
        vname = f"{path}/{video.default_filename.removesuffix('.mp4')}_videowaudio.mp4"
        os.rename(path+"/"+video.default_filename, vname)



label_valid=tk.Label(topframe,text="",font=('TimesNewRoman',15,'bold'),background="brown",fg="green")
label_valid.place(y="20",x="170",anchor="center")

def check_link():
    global url,count,download_videoaudio_button,download_audio_button,download_video_button
    err=False
    try:
        url=YouTube(link.get())
    except:
        err=True
        messagebox.showerror("Error", "Not a valid youtube link")
    else:
        count+=1

    finally:
        if not err:
            if count==1:
                label_valid.config(text="VALID URL",foreground="green")


                download_videoaudio_button=tk.Button(command=download_videaudio,text="Download Video w audio",fg="black",activeforeground="white",justify='left', font=('Arial',12,'bold'),
                                       activebackground="green",background="white",highlightbackground="black")
                download_videoaudio_button.place(x="230",y="430",anchor='w')

                download_audio_button=tk.Button(command=download_audio,text="Download Audio",fg="black",activeforeground="white",justify='left', font=('Arial',12,'bold'),
                                                activebackground="green",background="white",highlightbackground="black")
                download_audio_button.place(x="220",y="430",anchor="e")


                download_video_button=tk.Button(command=download_video,text="Download Video wo audio",fg="black",activeforeground="white",justify='left', font=('Arial',12,'bold'),
                                    activebackground="green",background="white",highlightbackground="black")
                download_video_button.place(x="250",y="470",anchor="center")
            else:
                label_valid.config(text="VALID URL",foreground="green")
                download_audio_button.place(x="220",y="430",anchor="e")
                download_video_button.place(x="250",y="470",anchor="center")
                download_videoaudio_button.place(x="230",y="430",anchor='w')
        elif err and count>=1:
            label_valid.config(text="NOT VALID URL", foreground="red")
            download_audio_button.place_forget()
            download_video_button.place_forget()
            download_videoaudio_button.place_forget()
        else:
            label_valid.config(text="NOT VALID URL",foreground="red")
        


       

    
    

link=StringVar()
textbox=tk.Entry(topframe,width="50",textvariable=link)
textbox.pack()

check_button=tk.Button(topframe,text="CHECK",command=check_link,fg="black",activeforeground="green",justify='left', font=('Arial',10)
                        ,background="white",highlightbackground="black")
check_button.pack(side="top",pady=("10","0"))

label=tk.Label(topframe,text="download location",font=('TimesNewRoman',14,'bold'),background="brown",fg="white")
label.pack(side="left",pady=("10","0"),padx=("60","40"))



#select location
def select_location():
    global path
    path=filedialog.askdirectory()
    path_label.config(text=path)

path_label=tk.Label(text="",font=('TimesNewRoman',10),background="brown",fg="white")
path_label.place(x="250", y="200",anchor="center")

select_button=tk.Button(topframe,command=select_location,text="select",fg="black",activeforeground="green",justify='left', font=('Arial',10)
                        ,background="white",highlightbackground="black")
select_button.pack(side="left",pady=("10","0"))






#bottomframe
#bottomframe = tk.Frame(window,background="brown")
#bottomframe.pack( side="bottom" )





def check_int_conn()->bool:
    url="https://www.google.com/"
    try:
        stat_code=urlreq.urlopen(url)
        return True
    except:
        messagebox.showerror("No internet connection", "You have no internet connection!")
        return False










check_int_conn()
window.mainloop()

