import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImage=PIL.Image.open(path).convert("L").resize((300,300))
    imageData=PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image=imageData

def openfile():
    fpath=fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root=tk.Tk()
root.geometry("400x350")

lbl=tk.Label(text="グレースケールに変換するアプリ ver.1.1")
btn = tk.Button(text="ファイルを開く",command=openfile)
lbl.pack()
imageLabel=tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
