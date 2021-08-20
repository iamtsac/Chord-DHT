import socket
import numpy as np

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


def find_successor(L, n):
    L = np.asarray(L)
    finger = L[L >= n].min()

    return finger

#def create_finger(nodes,finger_table):
def create_finger():
    nodes = [112,96,80,16,32,45,51,32,43,56,74,32,15,66,42]
    finger_table = {}
    m = 7
    max_value = 2**m
    nodes_sorted = sorted(nodes)
    for node in nodes_sorted:
        fingers = list()
        for i in range(m):
            hop = (node + pow(2,i)) 
            fingers.append(find_successor(nodes_sorted,hop%max_value))
        finger_table[node] = fingers
    print(finger_table)

create_finger()
