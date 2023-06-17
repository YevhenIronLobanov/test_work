import asyncio

async def send_data():
    reader, writer = await asyncio.open_connection('', 55000)
    print('Підключено до сервера')

    a = int(input('Введіть перше число: '))
    b = int(input('Введіть друге число: '))

    message = f'{a},{b}'.encode()
    writer.write(message)
    await writer.drain()

    data = await reader.read(100)
    response = data.decode()
    results = list(map(int, response.split(', ')))

    print('Отримано результати:')
    print(f'Додавання: {results[0]}')
    print(f'Віднімання: {results[1]}')
    print(f'Множення: {results[2]}')

    writer.close()
    await writer.wait_closed()

asyncio.run(send_data())