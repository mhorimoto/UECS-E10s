#! /usr/bin/env python3
import socket

def main():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        print(f"Listening on {host}:{port}")

        while True:
            data, addr = sock.recvfrom(1024)
            print(f"Received data: {data} from {addr}")

if __name__ == "__main__":
    main()
