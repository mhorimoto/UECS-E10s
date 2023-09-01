#! /usr/bin/env python3
#coding: utf-8
#
import socket
import netifaces
import os


def rx_test():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        print(f"Listening on {host}:{port}")

        while True:
            data, addr = sock.recvfrom(1024)
            print(f"Received data: {data} from {addr}")


def e10s_send(m,u,t,a):
    for i in netifaces.interfaces():
        if i=="lo":
            continue
        try:
            HOST = netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']
            print(HOST)
            break
        except:
            print(f"no {i} interface")
            continue
    ADDRESS = netifaces.ifaddresses(i)[netifaces.AF_INET][0]['broadcast']
    PORT = 16520
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR|socket.SO_BROADCAST, 1)
    sock.bind(('', PORT))

    ut = "<?xml version=\"1.0\" encode=\"utf-8\"?><UECS ver=\"1.00-E10s\"><MEMO>{0}</MEMO>"\
        "<URI>{1}</URI><TIME>{2}</TIME><AT>{3}</AT><IP>{4}</IP></UECS>".format(m,u,t,a,HOST)
    print(ut)
    print(PORT)
    print(ADDRESS)
    sock.sendto(ut.encode(),(ADDRESS,PORT))
    sock.close()


if __name__ == "__main__":
    e10s_send("TEST","http://test.com/test","20230901140000","1:1:2")
#    rx_test()
