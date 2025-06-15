__author__ = '城南小学2019(04)班 老煜'
__version__ = '7.0.0'
import os
import hashlib
from ttkbootstrap import *  #pip install ttkbootstrap
from ttkbootstrap.constants import *
import tkinter.filedialog as file
from tkinter import messagebox,simpledialog,IntVar
from random import choice
import windnd     #pip install windnd
from tkinter.ttk import Progressbar

username = os.getlogin()
s = ""
if os.path.exists(f"C:/Users/{username}/Documents/conf.txt") == True:
        with open(f"C:/Users/{username}/Documents/conf.txt") as conf:
            for line in conf:
                line.rstrip("\n")
                s = line
else:
    with open(f"C:/Users/{username}/Documents/conf.txt","w") as conf:
        conf.write("solar")
        s = "solar"

font = ('Consolas','10')
key = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
root = Window()
root.title('文件加解密工具')
root.resizable(0,0)
style = Style()
style.theme_use(s)
filemain = LabelFrame(root,text="文件处理")
filemain.grid(row=0,column=0)
opition = LabelFrame(root,text="选项")
opition.grid(row=1,column=0)

theme_name = style.theme_names()
theme_1 = Label(opition,text="选择主题：").grid(row=0,column=0)
theme_2 = Combobox(master=opition,
                 text=style.theme.name,
                 values=theme_name)
theme_2.config(state="readonly")
theme_2.grid(row=0,column=1,columnspan=1)
theme_2.current(theme_name.index(style.theme.name))
def change_theme(self):
    theme_value = theme_2.get()
    style.theme_use(theme_value)
    os.remove(f"C:/Users/{username}/Documents/conf.txt")
    with open(f"C:/Users/{username}/Documents/conf.txt","w") as conf:
        conf.write(theme_value)
    theme_2.selection_clear()
theme_2.bind('<<ComboboxSelected>>',change_theme)
checkvar = IntVar()
delsource = Checkbutton(opition,text="操作完成后删除源文件",variable=checkvar)
delsource.grid(row=0,column=2)

name = Label(filemain,text='加密或解密的文件(可拖入):').grid(row=0,column=0)
name_2 = Entry(filemain,font=font)
name_2.grid(row=0,column=1)

password_1 = Label(filemain,text='加密或解密的密码:').grid(row=1,column=0)
password_2 = Entry(filemain,font=font,show="*")
password_2.grid(row=1,column=1)
data_1 = Label(filemain,text='保存路径(可不填):').grid(row=2,column=0)
data_2 = Entry(filemain,font=font)
data_2.grid(row=2,column=1)


def main():
    name_1 = name_2.get()
    password = password_2.get()
    if os.path.exists(name_1) == True:
        pass
    else:
        messagebox.showerror('错误','文件不存在！')
        root.destroy()
    data = data_2.get()

    if name_1.split(".")[-1][-4:] == 'DATA':
        F = name_1.split(".")[-1].replace("DATA", "")
        if os.path.split(data)[0] == '':
            if os.path.split(name_1)[0] == '':
                data = '.'.join(list(os.path.split(name_1)[-1].split(".")[:-1])) + '.' + F
            else:
                data = os.path.split(name_1)[0] + '/' + '.'.join(list(os.path.split(name_1)[-1].split(".")[:-1])) + '.' + F
        else:
            data = data + '/' + '.'.join(list(os.path.split(name_1)[-1].split(".")[:-1])) + '.' + F
    else:
        # 保存路径
        if os.path.split(data)[0] == '':
            if os.path.split(name_1)[0] == '':
                data = name_1.split(".")[-1]
                data = os.path.split(name_1)[-1].split(".")[0] + '.' + data + 'DATA'
            else:
                data = name_1.split(".")[-1]
                data = os.path.split(name_1)[0] + '/' + '.'.join(list(os.path.split(name_1)[-1].split(".")[:-1])) + '.' + data + 'DATA'
        else:
            name_3 = name_1.split(".")[-1]
            data = data + '/' + '.'.join(list(os.path.split(name_1)[-1].split(".")[:-1])) + '.' + name_3 + 'DATA'



    source_size = os.path.getsize(name_1)
    a = open(name_1, "rb")
    b = open(data, "wb")




    hl = hashlib.md5()
    hl.update(password.encode(encoding='utf-8'))
    password_list = hl.hexdigest()

    hl.update(password_list.encode(encoding='utf-8'))
    password_list2 = hl.hexdigest()
    password_data = password_list+password_list2


    x = Window()
    x.title("进度")
    x.geometry("200x120")
    progress = Progressbar(x)
    progress.pack(pady=20)
    progress["maximum"] = source_size
    progress["value"] = 0
    count = 0  #索引
    for now in a:
        for nowByte in now:
            newByte = nowByte ^ ord(password_data[count % len(password_data)])
            count += 1
            b.write(bytes([newByte]))
        out_size = os.path.getsize(data)
        progress["value"] = out_size
        x.update()
    x.destroy()

    a.close()
    b.close()
    if checkvar.get() == 1:
        os.remove(name_1)
    root.destroy()

def openfile():
    s = file.askopenfilename(title='浏览文件',filetypes=[('所有文件','*')])
    name_2.delete(0,END)
    name_2.insert(0,s)
def savefile():
    d = file.askdirectory(title='保存文件路径')
    data_2.delete(0,END)
    data_2.insert(0,d)
def show():
    c = Window()
    c.title('关于')
    zh = '文件加密工具V7.0\nby 城南小学2019(4)班 老煜\n本工具由python开发而成，能够加解密\
文件。\n更新日志：\n\
V1.0\n\
第一个版本，无更新，为控制台程序。\n\
V2.0\n\
在1.0的基础上，增加了GUI界面，使其便利性大大提高。\n\
V2.1\n\
增加了生成密钥功能。\n\
V3.0\n\
增加文件拖入功能。\n\
V3.1\n\
增加了加密进度条。\n\
V4.0\n\
修复了大bug:文件名中有两个或以上句点时，后缀会出现错误。\n\
V5.0\n\
在4.0基础上，修复了文件名错误。\n\
V6.0\n\
在5.0基础上，增强密码框功能，更改GUI风格。\n\
V7.0\n\
在6.0基础上，增加了切换主题、删除原文件等功能。\n\
\n\
7.0版本发布日期：2025年4月13日。'
    z = Text(c)
    z.pack()
    z.insert(END,zh)
    z.config(state='disabled')
def keys():
    if messagebox.askyesno('生成密钥','本功能会随机生成密钥，务必全部复制！是否继续？'):
        length = int(simpledialog.askstring('生成密钥','输入要生成的密钥的长度:'))
        pas = ''
        for i in range(length):
            h = choice(key)
            pas = pas + str(h)
        password_2.delete(0,END)
        password_2.insert(0,pas)
        pwd_2.delete(0,END)
        pwd_2.insert(0,pas)
def dragged_file(files):
    file = '\n'.join(item.decode('gbk') for item in files)
    name_2.delete(0,END)
    name_2.insert(0,file)
def show_pwd():
    password = password_2.get()
    messagebox.showinfo("密码",f"密码为：{password}")
name_3 = Button(filemain,text='浏览...',command=openfile,bootstyle=(INFO,OUTLINE)).grid(row=0,column=2)
data_3 = Button(filemain,text='浏览...',command=savefile,bootstyle=(INFO,OUTLINE)).grid(row=2,column=2)
password_3 = Button(filemain,text='生成密钥',command=keys,bootstyle=(INFO,OUTLINE)).grid(row=1,column=2)
button = Button(filemain,text='加密或解密',command=main,bootstyle=(INFO,OUTLINE)).grid(row=3,column=1)
m = Menu(root,tearoff=0)
tl = Menu(m,tearoff=0)
tl.add_command(label="显示密码",command=show_pwd)
tl.add_separator()
m.add_cascade(label="功能",menu=tl)
ab = Menu(m,tearoff=0)
ab.add_command(label='关于...',command=show)
ab.add_separator()
m.add_cascade(label='关于',menu=ab)
root.config(menu=m)
windnd.hook_dropfiles(root,func=dragged_file)
root.mainloop()

