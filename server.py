import socket
import numpy as np

"""

creating nodes 

"""

HOST='localhost'
PORT=65432

def check_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

while(check_port_in_use(PORT)):
    PORT+=1

node_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
node_socket.bind(("localhost",PORT))
node_socket.listen()
print(PORT)

"""
configuring chord

nodes = [112,96,80,16,32,45,51,32,43,56,74,32,15,66,42]
finger_table = {}
m = 4
max_value = max(nodes) + 1

"""



def find_successor(L, n):
    L = np.asarray(L)
    finger = L[L >= n].min()

    return finger

def create_finger(nodes,finger_table):
    nodes_sorted = sorted(nodes)
    for node in nodes_sorted:
        fingers = list()
        for i in range(m):
            hop = (node + pow(2,i)) % max_value
            fingers.append(find_successor(nodes_sorted,hop))
        finger_table[node] = fingers.copy()

while True:
    pass
