#!/usr/bin/python
# -*- coding: Shift-JIS -*-

# 数当てゲーム
# ランダムに決められた数字（1～100）を当てる

import random as rd

# 正解時の画面表示処理
def disp_msg(count):
    msg = ""
    if count < 5 :
        msg = "Wonderful!"
    elif count < 10 :
        msg = "Great!"
    else:
        msg = "Good!"

    print(msg ,"正解です!!!")
    return

# メイン処理
print("**** 数当てゲーム ****")
print("1-100の数字を入力してください。end入力で終了")

ans = rd.randint(1,100)
#print("[DBG] ans=",ans)

cnt = 0
while True:
    num = input("数字を入力してください > ")
    if num == "end":
        break
    num = int(num)
    if num < ans :
        print("・・・もっと大きい")
    elif ans < num :
        print("・・・もっと小さい")
    elif ans == num :
        disp_msg(cnt)
        break
    else:
        print("[ERR] num=",num)
    cnt = cnt + 1