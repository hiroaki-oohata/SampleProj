#!/usr/bin/python
# -*- coding: Shift-JIS -*-

# �����ăQ�[��
# �����_���Ɍ��߂�ꂽ�����i1�`100�j�𓖂Ă�

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

    print(msg ,"�����ł�!!!")
    return

# ���C������
print("**** �����ăQ�[�� ****")
print("1-100�̐�������͂��Ă��������Bend���͂ŏI��")

ans = rd.randint(1,100)
#print("[DBG] ans=",ans)

cnt = 0
while True:
    num = input("��������͂��Ă������� > ")
    if num == "end":
        break
    num = int(num)
    if num < ans :
        print("�E�E�E�����Ƒ傫��")
    elif ans < num :
        print("�E�E�E�����Ə�����")
    elif ans == num :
        disp_msg(cnt)
        break
    else:
        print("[ERR] num=",num)
    cnt = cnt + 1