import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytlink = link.get()
        ytobj = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytobj.streams.get_highest_resolution()
        title.configure(text=ytobj.title, text_color="white")
        finish_label.configure(text="")
        video.download()
        finish_label.configure(text="Your Downloading is finished")
    except:
        finish_label.configure(text="Invalid Link", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_dowmloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_dowmloaded / total_size * 100
    per = str(int(percentage_of_completion))
    p_percentage.configure(text=per + "%")
    p_percentage.update()

    # update Progress Bar:
    progress_bar.set(float(percentage_of_completion) / 100)


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


# Adding UI
title = customtkinter.CTkLabel(app, text="Insert the video link here")
title.pack(padx=50, pady=50)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finish Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()


# Progress Bar
p_percentage = customtkinter.CTkLabel(app, text="0%")
p_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)


# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)


# Run App
app.mainloop()
