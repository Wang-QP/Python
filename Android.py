import os
from time import sleep

#自动触控的坐标
def ldb(x,y):
	os.system('adb shell input tap {} {}'.format(x,y))

if __name__ == '__main__':
	for i in range(100):
		ldb(200,800)
		sleep(0.2)