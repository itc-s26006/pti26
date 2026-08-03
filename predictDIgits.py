import sklearn.datasets#数字の学習データを使えるようにする
import sklearn.svm　#AI学習を使えるようにする
import PIL.Image　#画像を開くためにの機能を使えるようにする
import numpy

def imageTOData(filename):#画像を数字のデータに変換する関数
    grayImage=PIL.Image.open(filename).convert("L")#画像を開いて、白黒画像にする。
    grayImage=grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)

    numImage= numpy.asarray(grayImage,dtype = float)
    numImage=16-numpy.floor(17*numImage/256)
    numImage=numImage.flatten()
    
    return numImage
#数字を予測する
def predictDigits(data):
    digits=sklearn.datasets.load_digits()
    clf=sklearn.svm.SVC(gamma=0.001)#機械学習させる
    clf.fit(digits.data,digits.target)
    n=clf.predict([data])#予測結果を表示する
    print("予測=",n)
data=imageTOData("2.png")#画像ファイルを数値リストに変換する
predictDigits(data)#数字を予測する

