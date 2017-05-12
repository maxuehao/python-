#-*- coding: UTF-8 -*-
import socket
from time import ctime
import threading

#创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9996))
#调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print('%s \nWaiting for connection...'%ctime())

#处理客户端请求函数
def tcplink(conn,addr):
	print 'Accept new connection from：%s'% str(addr)
	#向客户端发送数据
	conn.send(('Accept connection OK...').encode('utf-8'))
	#循环处理客户端请求
	while True:
		#接受来自客户端数据
		date = conn.recv(1024)
		if not date:
			print '%s \nconnection closed:%s ' %(ctime(),str(addr))
			break
		print '%s \nconnection from %s:%s' % (ctime(),addr,date)
	#关闭套接字，释放资源
	sock.close()

if __name__ == '__main__':
	#永久循环来接受来自客户端的连接
	while True:
		#accept()会等待并返回一个客户端的连接:
		conn, addr = s.accept()
		#每个新连接都开辟新的线程处理
		t = threading.Thread(target=tcplink, args=(conn, addr))
		t.start()
