'''
# 导入tkinter模块下面所有方法
from tkinter import *

# 创建一个主窗口
root = Tk()

# 是设置最小大小
root.minsize(300,300)

# 创建一个button,加入主窗口中
btn1 = Button(root,text="按钮1")
btn1.grid(row=0,column=0,columnspan=2,ipadx=30)

btn2 = Button(root,text="按钮2")
btn2.grid(row=0,column=2)

btn3 = Button(root,text="按钮3")
btn3.grid(row=0,column=3)

btn4 = Button(root,text="按钮4")
btn4.grid(row=1,column=0)

btn5 = Button(root,text="按钮5")
btn5.grid(row=1,column=1,rowspan=2,ipady=15)

btn6 = Button(root,text="按钮6")
btn6.grid(row=1,column=2,columnspan=2,ipadx=30)

btn7 = Button(root,text="按钮7")
btn7.grid(row=2,column=0)

btn8 = Button(root,text="按钮8")
btn8.grid(row=2,column=2,ipadx=30)
# 加入消息循环
root.mainloop()

from tkinter import *

root = Tk()
root.minsize(300,300)

but1 = Button(root,text='按钮1')
but1.place(x=0,y=0,height=30)

but2 = Button(root,text='按钮2')
but2.place(x=60,y=0,height=30)

but3 = Button(root,text='按钮3')
but3.place(x=120,y=0,height=30)

but4 = Button(root,text='按钮4')
but4.place(x=0,y=30,height=30)

but5 = Button(root,text='按钮5')
but5.place(x=60,y=30,height=30)

but6 = Button(root,text='按钮6')
but6.place(x=120,y=30,height=30)

root.mainloop()


from tkinter import *

root = Tk()
root.minsize(300,300)
but1 = Button(root,text='按钮1')
but1.place(relx=0,rely=0,relheight=0.1)

but2 = Button(root,text='按钮2')
but2.place(relx=0.2,rely=0,relheight=0.1)

but3 = Button(root,text='按钮3')
but3.place(relx=0.4,rely=0,relheight=0.1)

but4 = Button(root,text='按钮4')
but4.place(relx=0,rely=0.1,relheight=0.1)

but5 = Button(root,text='按钮5',font=20,bg="blue")
but5.place(relx=0.2,rely=0.1,relheight=0.1,relwidth=0.4)

but6 = Button(root,text='按钮6')
but6.place()

root.mainloop()

from tkinter import *
root = Tk()
#定义点击菜单触发的方法
def hello():
    print("hello!")

def open_f():
    print("正在打开文件")
#创建总菜单
menubar = Menu(root,bg="pink")

# 创建一个下拉菜单，并且加入文件菜单
filemenu = Menu(menubar)

#创建下来菜单的选项
filemenu.add_command(label="Open", command=open_f)
filemenu.add_command(label="Save", command=hello)
#创建下拉菜单的分割线
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

#将文件菜单作为下拉菜单添加到总菜单中，并且将命名为File
menubar.add_cascade(label="File", menu=filemenu)


# 显示总菜单
root.config(menu=menubar)
root.mainloop()


# 导入tkinter模块下面所有方法
from tkinter import *
import tkinter.messagebox

# 创建一个主窗口
root = Tk()

# 是设置最小大小
root.minsize(300,300)

# 定义一个函数
def info():
    resault = tkinter.messagebox.askretrycancel('友情提示','你的机器已超载,请更换机器')
    print(resault)

# 创建一个button,加入主窗口中
btn1 = Button(root,text="显示信息对话框",height=2,bg="#999",command=info)
btn1.grid(row=0,column=0,columnspan=2,ipadx=30)

btn2 = Button(root,text="按钮2")
btn2.grid(row=0,column=2)

btn3 = Button(root,text="按钮3")
btn3.grid(row=0,column=3)

btn4 = Button(root,text="按钮4")
btn4.grid(row=1,column=0)

btn5 = Button(root,text="按钮5")
btn5.grid(row=1,column=1,rowspan=2,ipady=15)

btn6 = Button(root,text="按钮6")
btn6.grid(row=1,column=2,columnspan=2,ipadx=30)

btn7 = Button(root,text="按钮7")
btn7.grid(row=2,column=0)

btn8 = Button(root,text="按钮8")
btn8.grid(row=2,column=2)
# 加入消息循环
root.mainloop()

from tkinter import *

root=Tk()
root.minsize(400,400)
frame1 = Frame(root,bg="red",width=150,height=80)
btn1 = Button(frame1,text="按钮1").pack()
label = Label(frame1,text="hhhhhh").pack()
frame1.pack(side="left")

frame2 = Frame(root,bg="blue",width=200,height=200)
label = Label(frame2,text="ooooooo").pack()

frame2.pack()
root.mainloop()
'''
from tkinter import *
root = Tk()
root.minsize(300,300)
def openwindow():
    resault = Toplevel(bg="yellow",height=100,width=100)
    resault.title('这是一个新窗口')
    resault['bg']="red"
    print(resault)

btn = Button(root,text="弹出一个新窗口",command=openwindow).pack()
root.mainloop()