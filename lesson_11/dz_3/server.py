import socket
def words_count (received_message):
    words = received_message
    word_count_ = words.split()
    return len(word_count_)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Запущено роботу сервера (для зупинки роботи сервера натисніть Ctrl+C)')

while True:
    conn, addr = sock.accept()
    print('Підключено:', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        received_message = data.decode('UTF-8')
        print('Client:', received_message)
        if received_message == 'Клієнт припинив роботу.':
            break

        result = str(words_count(received_message))
        conn.send(result.encode('UTF-8'))
conn.close()