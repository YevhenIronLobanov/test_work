import asyncio

# Створюємо функції для здійснення операцій
async def add(a, b):
    await asyncio.sleep(1)
    return a + b

async def subtr(a, b):
    await asyncio.sleep(1)
    return a - b

async def mult(a, b):
    await asyncio.sleep(1)
    return a * b

# Обробляємо підключення клієнта
async def handl_client(reader, writer):
    peername = writer.get_extra_info('peername')
    print(f'Підключено клієнта: {peername}')

    data = await reader.read(100)
    message = data.decode()
    a, b = map(int, message.split(','))

    # Визначаю задачі та виконую
    tasks = [
        asyncio.create_task(add(a, b)),
        asyncio.create_task(subtr(a, b)),
        asyncio.create_task(mult(a, b))
    ]
    await asyncio.wait(tasks)

    # Отримую результати
    results = [task.result() for task in tasks]
    response = ', '.join(map(str, results)).encode()
    writer.write(response)
    await writer.drain()
    writer.close()

# Запускаєм сервер
async def starter_server():
    server = await asyncio.start_server(handl_client, '', 55000)
    print(f'Запущенно роботу сервера. ')

    async with server:
        await server.serve_forever()

# Запускаємо сервер в циклі подій asyncio
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(starter_server())
ioloop.close()
