import sys
import socket
import logging
from multiprocessing import Process
import time  # Import time library

time.sleep(5)


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
    return


def create_process():
    p = Process(target=kirim_data)
    p.start()
    p.join()


if __name__ == '__main__':
    process_count = 0  
    start_time = time.time()  
    while time.time() - start_time < 30:  
        create_process()
        process_count += 1  # Update counter di sini
    # Cetak jumlah proses yang telah dibuat
    logging.warning(f"Total processes created: {process_count}")