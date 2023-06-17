import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Запущено роботу сервера (для зупинки роботи сервера натисніть Ctrl+C_')
while True:
    conn, addr = sock.accept()
    print('Підключено:', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        received_message = data.decode('UTF-8')
        print('Клієнт:', received_message)
        if received_message == 'Клієнт припинив роботу.':
            break
        answer = input('Сервер: ')
        conn.send(bytes(answer, encoding='UTF-8'))
    conn.close()




