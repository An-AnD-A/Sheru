# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:11:29 2021

@author: anand
"""

import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVER,PORT))

def handle_client(conn, addr):
    pass

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args = (conn,addr))
        thread.start()
