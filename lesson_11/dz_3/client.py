import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
print('Для того, щоб почати спілкування введіть повідомлення (щоб завершити, введіть "quit"')
while True:
    message = input('Клієнт: ')
    if message != 'quit':
        sock.send(bytes(message, encoding='UTF-8'))
    else:
        sock.send(bytes('Клієнт припинив роботу.', encoding='UTF-8'))
        break
    data = sock.recv(1024)
    print('Сервер:', data.decode('UTF-8'))
sock.close()

