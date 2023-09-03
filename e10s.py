#! /usr/bin/env python3
#coding: utf-8
#
import socket
import netifaces

def send(m,u="",t="",a=""):
    if m=="":
        return
    if u!="":
        u1="<URI>{0}</URI>".format(u)
    else:
        u1=""
    if t!="":
        t1 = "<TIME>{0}</TIME>".format(t)
    else:
        t1 = ""
    if a!="":
        a1 = "<AT>{0}</AT>".format(a)
    else:
        a1 = ""

    for i in netifaces.interfaces():
        if i=="lo":
            continue
        try:
            HOST = netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']
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
        "{1}{2}{3}<IP>{4}</IP></UECS>".format(m,u1,t1,a1,HOST)
    sock.sendto(ut.encode('utf-8'),(ADDRESS,PORT))
    sock.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv)==5:
        send(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
