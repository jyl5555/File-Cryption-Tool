__author__ = '城南小学2019(04)班 老煜'
__vertion__ = '2.0.0'
import os
import hashlib
from tkinter import Label,Entry,Button,Tk,messagebox,Menu
import tkinter.filedialog as file
font = ('Consolas','10')

root = Tk()
root.title('文件加解密工具')
name = Label(root,text='加密或解密的文件名:').grid(row=1,column=1)
name_2 = Entry(root,font=font)
name_2.grid(row=1,column=2)

password_1 = Label(root,text='加密或解密的密码或密钥:').grid(row=2,column=1)
password_2 = Entry(root,font=font)
password_2.grid(row=2,column=2)
data_1 = Label(root,text='保存路径(可不填):').grid(row=3,column=1)
data_2 = Entry(root,font=font)
data_2.grid(row=3,column=2)



def main():
    name_1 = name_2.get()
    password = password_2.get()
    if os.path.exists(name_1) == True:
        pass
    else:
        messagebox.showerror('错误','文件不存在！')
        root.destroy()
    data = data_2.get()

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
    root.destroy()
 
def openfile():
    s = file.askopenfilename(title='浏览文件',filetypes=[('所有文件','*')])
    name_2.insert(0,s)
def savefile():
    d = file.askdirectory(title='保存文件路径')
    data_2.insert(0,d)
def show():
    c = Tk()
    c.title('关于')
    zh='文件加密工具V2.0\nby 城南小学2019(4)班 老煜\n本工具由一个小学生在机房练习无聊之时\n用python开发而成，可以加解密文件。'
    z = Label(c,text=zh)
    z.pack()
name_3 = Button(root,text='浏览...',command=openfile).grid(row=1,column=3)
data_3 = Button(root,text='浏览...',command=savefile).grid(row=3,column=3)
button = Button(root,text='加密或解密',command=main).grid(row=4,column=2)
m = Menu(root,tearoff=0)
ab = Menu(m,tearoff=0)
ab.add_command(label='关于...',command=show)
ab.add_separator()
m.add_cascade(label='关于',menu=ab)
root.config(menu=m)
root.mainloop()

