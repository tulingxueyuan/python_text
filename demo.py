# 导入tkinter
import tkinter

# 创建一个主窗口
root = tkinter.Tk()

# 定义最大大小
# root.maxsize(500,500)

# 定义最小大小
root.minsize(300,300)

# 创建一个button,并加入主窗口
but = tkinter.Button(root,text="我是一个按钮")
but.pack()

# 加入消息循环
root.mainloop()