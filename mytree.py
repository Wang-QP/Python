import os

ls = input("")
def f(name,n):
	mylist = os.listdir(name)
	for var in mylist:
		print("-"*n + "|" + var)
		var = os.path.join(name,var)
		if(os.path.isdir(var)):
			f(var,n+2)
if not ls:
	ls = 'D:\\daima\\python'
f(ls,0)
