import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("127.0.0.1", 9090)
print('Connected to {}, port {}'.format(*server_address))
sock.connect(server_address)

while True:
    try:
        message = input().upper()
        print(f'Отправка: {message}')
        sock.sendall(message.encode())
        if message == "END":
            print("BROKEN!!!")
            break

        result = sock.recv(1048).decode()
        print(result)
    except Exception as error:
        print(f"{error} was thrown")

sock.close()
