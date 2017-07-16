import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))

mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
data = mysock.recv(414)
print(data)

mysock.close()
