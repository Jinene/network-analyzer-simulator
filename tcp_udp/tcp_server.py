import socket

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("TCP Server listening...")

conn, addr = server.accept()
print(f"Connected to {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Client: {data.decode()}")
    conn.sendall(b"ACK from server")

conn.close()
