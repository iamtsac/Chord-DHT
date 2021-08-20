import pickle
import socket

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004
data = []

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
while True:
    Input = input('Hey there: ')
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    data.append(res)
    data_arr = pickle.loads(b"".join(data))
    print(data_arr)

ClientMultiSocket.close()
