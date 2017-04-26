#!/usr/bin/env python

import socket
import sys

# get variables from commandline
target_host = sys.argv[1]
target_port = 25
target_names = ["georgia","john", "jett", "ezra", "admin"]

# create connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the client
client.connect((target_host, target_port))
recv_len = 1
response = ""

while recv_len:
    data = client.recv(4096)
    recv_len = len(data)
    response+= data
    if recv_len < 4096:
        print "break"
        break

# send data
for user_name in target_names:
    print "Verifying user: " + user_name
    client.send(str("VRFY " + user_name + "\n"))
    while recv_len:
        response=''
        data = ""
        data = client.recv(4096)
        recv_len = len(data)
        response+= data
        print response
        if recv_len < 4096:
            break
 
client.close()
