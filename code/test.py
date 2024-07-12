#!/usr/bin/python
# -*- coding: Shift-JIS -*-

import random as rd

# �ｽ�ｽ�ｽ�ｽ�ｽ�ｽ�ｽﾌ会ｿｽﾊ表�ｽ�ｽ�ｽ�ｽ�ｽ�ｽ
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

print("**** asa ****")
print("1-100譁�ｭ怜喧縺")

ans = rd.randint(1,100)
#print("[DBG] ans=",ans)

cnt = 0
while True:
    num = input("縺 > ")
    if num == "end":
        break
    num = int(num)
    if num < ans :
        print("�薙∴�暦ｽ")
    elif ans < num :
        print("�輔≧縺�ｽ")
    elif ans == num :
        disp_msg(cnt)
        break
    else:
        print("[ERR] num=",num)
    cnt = cnt + 1