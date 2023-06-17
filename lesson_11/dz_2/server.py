import socket
def chat_bot(received_message):
    if received_message == 'Привіт' or received_message == 'Добрий день':
        answer = 'Добрий день. Чим можу вам допомогти?'
    elif received_message == 'Є в наявності товар за кодом 001':
        answer = 'Товар є в наявності.'
    elif received_message == 'Яка вартість зазначеного товару?':
        answer = '500 грн.'
    elif received_message == 'Є в наявності товар за кодом 002':
        answer = 'Товар відсутній.'
    else:
        answer = 'Інформація відсутня.'
    return answer
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

        answer = chat_bot(received_message)
        conn.send(answer.encode('UTF-8'))
conn.close ()
