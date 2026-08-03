from turtle import *# タートルグラフィックスを使う準備
shape ("turtle")# 亀の登場
col = ["red","blue","green","brown","black"]

for i in range(5): # 以下を5回繰り替えす
       color(col[i])# 線の色を変える
       forward(200)#まっすぐ200進むこと
       left(144)#144度曲がること
done()# おしまい※追記:これインデントずらさないとfor 構文のなかに入っちゃうので注意
