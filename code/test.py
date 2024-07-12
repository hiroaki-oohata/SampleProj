#!/usr/bin/python
# -*- coding: Shift-JIS -*-

import random as rd

# �������̉�ʕ\������
def disp_msg(count):
    msg = ""
    if count < 5 :
        msg = "Wonderful!"
    elif count < 10 :
        msg = "Great!"
    else:
        msg = "Good!"

    print(msg ,"Test")
    return

print("**** asa ****")
print("1-100文字化け")

ans = rd.randint(1,100)
#print("[DBG] ans=",ans)

cnt = 0
while True:
    num = input("あ > ")
    if num == "end":
        break
    num = int(num)
    if num < ans :
        print("ｓえｗｗ")
    elif ans < num :
        print("５うぇｗ")
    elif ans == num :
        disp_msg(cnt)
        break
    else:
        print("[ERR] num=",num)
    cnt = cnt + 1