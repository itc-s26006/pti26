from turtle import *# タートルグラフィックスを使う準備
shape ("turtle")# 亀の登場
col = ["orange","limegreen","gold","plum","tomato"]

for i in range(5): # 以下を5回繰り替えす
       color(col[i])# 線の色を変える
       circle(100) #半径100の円を書く
       left(72)  #72度曲がること
done()  # おしまい※追記:これインデントずらさないとfor 構文のなかに入っちゃうので注意
