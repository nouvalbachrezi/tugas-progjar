import sys
import socket
import logging
import threading
import time

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('localhost', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode())
        # Look for the response
        data = sock.recv(32)
        logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()

def create_thread():
    t = threading.Thread(target=kirim_data)
    t.start()
    t.join()

if __name__ == '__main__':
    thread_count = [0]  # Menggunakan list sebagai wadah mutable untuk thread_count
    start_time = time.time()

    def run_threads():
        while True:
            if time.time() - start_time >= 5:
                break
            create_thread()
            thread_count[0] += 1  # Mengakses dan memperbarui nilai thread_count melalui list

    run_threads()

    logging.warning(f"Total threads created: {thread_count[0]}")
