import socket

HOST='localhost'
PORT=9000

def check_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

while(check_port_in_use(PORT)):
    PORT+=1

node_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
node_socket.bind(("localhost",PORT))
node_socket.listen()
print(PORT)

while True:
    pass
