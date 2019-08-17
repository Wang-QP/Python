import win32gui
import win32con
import win32clipboard as w
import time

#发送的消息
msg = "发送的消息"
#窗口名字
name = "窗口名字"
#将测试消息复制到剪切板中
w.OpenClipboard()
w.EmptyClipboard()

w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
w.CloseClipboard()
#获取窗口句柄
handle = win32gui.FindWindow(None, name)
#while 1==1:
while True:
    #填充消息
    win32gui.SendMessage(handle, 770, 0, 0)
    #回车发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.8)