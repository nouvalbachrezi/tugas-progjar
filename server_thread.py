from socket import *
import socket
import threading
import logging
import time
import sys


class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = self.connection.recv(32)
            if data:
                logging.warning(
                    f"[SERVER] received {data} from {self.address}")

        
                if data.startswith(b'TIME') and data.endswith(b'\r\n'):
                    # Membuat string response sesuai format yang diminta
                    current_time = time.strftime("%H:%M:%S")
                    response = f"JAM {current_time}\r\n"
                    logging.warning(
                        f"[SERVER] sending {response} to {self.address}")
                    self.connection.sendall(response.encode('utf-8'))
                else:
                    break
            else:
                break
        self.connection.close()


class TimeServer(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 45000))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    svr = TimeServer()
    svr.start()


if __name__ == "__main__":
    main()