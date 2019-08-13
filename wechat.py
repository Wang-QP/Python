import itchat
import time
print("扫码")
itchat.auto_login(hotReload = True)
boom_remark_name = input("好友备注")
message = "发送内容"
boom_obj = itchat.search_friends(remarkName = boom_remark_name)[0]['UserName']
print(boom_obj)
index = 0
while True:
	time.sleep(2.3)
	print("sending...")
	itchat.send_msg(message,toUserName = boom_obj)