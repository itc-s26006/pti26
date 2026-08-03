import tkinter as tk #ウィンドウを表示するモジュール
import tkinter.filedialog as fd #ファイルダイアログを使うモジュール
import PIL.Image #画像を扱うモジュール
import PIL.ImageTk #tkinterで作った画面上にがぞうを表示させるモジュール

def dispPhoto(path):#画像ファイルを表示する関数
          #画面を読み込んで、グレーススケールか（モノクロ）に変換する
    newImage=PIL.Image.open(path).convert("L").resize((300,300))

    imageDeta=PIL.ImageTk.PhotoImage(newImage)#イメージをラベルに表示する
    imageLabel.configure(image = imageDeta)
    imageLabel.image = imageDeta

def openfile():
    fpath=fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root=tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く",command=openfile)
imageLabel=tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
