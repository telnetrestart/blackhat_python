#!/usr/bin/env python
import socket
import os

# host to listen on
host = "192.168.1.5"

# create a raw socket and bind it to the public interface
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP
    
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

# we want the IP headers included in the capture
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# if we're using Windows, we need to send an IOCTL
# to set up promiscuous mode
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
# read in a single packet
print sniffer.recvfrom(6556)

# if we're using Windows, turn off promiscuous mode
if os.name == "nt":
    SNIFFER.IOCTL(SOCKET.sio_rcvall, SOCKET.rcvall_off)
