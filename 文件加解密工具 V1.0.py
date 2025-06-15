import os
import hashlib
from tkinter import Label,Entry,Button,Tk

print("-------------------------------------软件加密工具-------------------------------------\n")
name_1 = input('输入要加密或解密的文件名含后缀：')
#判断是否存在该文件
if os.path.exists(name_1) == True:
    pass
else:
    print('请检查是否路径错误或不存在该文件！！！！')
    os.system('pause')
    exit()
 
password = input('请输入要加密或解密的密码：')
data = input('输入要保存文件的路径位置(可不填)：')
 
 
if name_1.split(".")[1][-4:] == 'DATA':
    F = name_1.split(".")[1].replace("DATA", "")
    if os.path.split(data)[0] == '':
        if os.path.split(name_1)[0] == '':
            data = os.path.split(name_1)[-1].split(".")[0] + '.' + F
        else:
            data = os.path.split(name_1)[0] + '/' + os.path.split(name_1)[-1].split(".")[0] + '.' + F
    else:
        data = data + '/' + os.path.split(name_1)[-1].split(".")[0] + '.' + F
else:
    # 保存路径
    if os.path.split(data)[0] == '':
        if os.path.split(name_1)[0] == '':
            data = name_1.split(".")[1]
            data = os.path.split(name_1)[-1].split(".")[0] + '.' + data + 'DATA'
        else:
            data = name_1.split(".")[1]
            data = os.path.split(name_1)[0] + '/' + os.path.split(name_1)[-1].split(".")[0] + '.' + data + 'DATA'
    else:
        name_3 = name_1.split(".")[1]
        data = data + '/' + os.path.split(name_1)[-1].split(".")[0] + '.' + name_3 + 'DATA'
 
 
 
a = open(name_1, "rb")
b = open(data, "wb")
 
 
 

hl = hashlib.md5()
hl.update(password.encode(encoding='utf-8'))
password_list = hl.hexdigest()
 
hl.update(password_list.encode(encoding='utf-8'))
password_list2 = hl.hexdigest()
password_data = password_list+password_list2
 

def Encryption_and_decryption():
    count = 0  #索引
    for now in a:
        for nowByte in now:
            newByte = nowByte ^ ord(password_data[count % len(password_data)])
            count += 1
            b.write(bytes([newByte]))
Encryption_and_decryption()
a.close()
b.close()
 
os.system('pause')
