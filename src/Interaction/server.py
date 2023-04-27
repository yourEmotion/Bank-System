import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 9090))
sock.listen(1)


print('Awaiting...')
connection, address = sock.accept()
try:
    print('Connected to:', address)
    while True:
        data = connection.recv(1028).decode()
        print(f'Get: {data}')
        data = data.lower()
        if data == "end":
            print("That's all!")
            break

        result = "Done successfully!!!"
        connection.sendall(result.encode())

except Exception:
    print("Something went wrong...")

sock.close()
