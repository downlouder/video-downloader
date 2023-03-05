from tkinter import *
from tkinter.ttk import *
from threading import Thread
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, window):
        self.window = window
        self.window.title("YouTube Downloader")
        self.label_url = Label(window, text="Enter the video URL:", font ='arial 12')
        self.label_url.grid(column=0, row=0, padx=10, pady=10)
        self.entry_url = Entry(window, width=50)
        self.entry_url.grid(column=1, row=0, padx=10, pady=10)
        self.button_download = Button(window, text="Download", command=self.start_download)
        self.button_download.grid(column=2, row=0, padx=10, pady=10)
        self.label_status = Label(window, text="")
        self.label_status.grid(column=0, row=2, columnspan=3)

    def start_download(self):
        url = self.entry_url.get()
        self.entry_url.delete(0, END)
        self.label_status.config(text='', font ='arial 10')
        thread = Thread(target=self.download_video, args=(url,))
        thread.start()

    def download_video(self, url):
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            file_size = stream.filesize
            self.label_status.config(text="Downloading...")
            filename = stream.default_filename
            stream.download()
            self.label_status.config(text="Download complete!")
        
        except Exception as e:
            self.label_status.config(text='Please enter correct URL', font ='arial 10')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    window = Tk()
    window.resizable(0,0)
    downloader = YouTubeDownloader(window)
    downloader.run()