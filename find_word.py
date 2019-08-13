import os

ls = input("")
def f(file,name):
	mylist = os.listdir(file)
	for var in mylist:
		var = os.path.join(file,var)
		if(os.path.isdir(var)):
			f(var)
		else:
			with open(var,"rb") as fp:
				a = fp.readlines()
				for w in a:
					if name.encode("utf-8") in w:
						print(var)

if not ls:
	ls = '文件目录'
name = "查询文字"
f(ls,name)