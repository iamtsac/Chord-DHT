import socket
import pickle
import os
from _thread import *

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
i = 0
response = list()
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection,response):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        if not data:
            break
        print(response)
        print(pickle.dumps(response))
        connection.sendall(pickle.dumps(response))
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    i+=1
    response.append(i)
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    #start_new_thread(multi_threaded_client, (Client,response ))
    multi_threaded_client(Client,response)
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
