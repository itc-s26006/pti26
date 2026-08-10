import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

import sklearn.datasets
import sklearn.svm
import numpy


# 画像ファイルを数値リストに変換
def imageToData(filename):

    # 画像を8×8のグレースケールに変換
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize(
        (8, 8),
        PIL.Image.Resampling.LANCZOS
    )

    # 8×8の画像を300×300に拡大して表示
    dispImage = PIL.ImageTk.PhotoImage(
        grayImage.resize((300, 300), resample=0)
    )

    imageLabel.configure(image=dispImage)
    imageLabel.image = dispImage

    # 数値リストに変換
    numImage = numpy.asarray(grayImage, dtype=float)

    # 0～255の画像を0～16に変換
    numImage = 16 - numpy.floor(17 * numImage / 256)

    # 8×8を1次元の64個のデータにする
    numImage = numImage.flatten()

    return numImage


# 数字を判定する
def predictDigits(data):

    # 手書き数字のデータセットを読み込む
    digits = sklearn.datasets.load_digits()

    # SVMという機械学習モデルを作る
    clf = sklearn.svm.SVC(gamma=0.001)

    # 学習する
    clf.fit(digits.data, digits.target)

    # 数字を予測する
    n = clf.predict([data])

    print(f"学習履歴:[{n[0]}]")
    # 結果を画面に表示
    textLabel.configure(
        text="この画像は" + str(n[0]) + "です!"
    )


# ファイルを開く
def openfile():

    fpath = fd.askopenfilename()

    if fpath:
        data = imageToData(fpath)

        # 数字を判定
        predictDigits(data)


# アプリのウィンドウを作る
root = tk.Tk()
root.geometry("400x400")


# ファイルを開くボタン
btn = tk.Button(root,text="ファイルを開く",command=openfile)
imageLabel = tk.Label()


# 画像を表示する場所
imageLabel = tk.Label(root)


# 判定結果を表示する場所
textLabel = tk.Label(
    root,
    text="ここに判定結果が表示されます",
    font=("Arial", 16)
)


btn.pack()
imageLabel.pack()
textLabel.pack()


# アプリを開始
root.mainloop()

print("終了")
