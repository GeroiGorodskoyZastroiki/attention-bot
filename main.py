import os
import time
import random
from pyrogram import Client
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Загрузка переменных окружения из файла .env
load_dotenv('.env')

# Получение user_id из .env файла
user_id = int(os.getenv('USER_ID'))
api_id = int(os.getenv('API_ID'))
api_hash = str(os.getenv('API_HASH'))

# Инициализация клиента Pyrogram
app = Client('my_account', api_id=api_id, api_hash=api_hash)

# Функция для отправки сообщения
async def send_random_message():
    while True:
        # Генерация случайного времени от 6 до 12 часов
        # delay_hours = random.randint(6, 12)
        delay_hours = random.randint(0, 0)
        # delay_minutes = random.randint(0, 59)
        delay_minutes = random.randint(40, 41)
        random_time = timedelta(hours=delay_hours, minutes=delay_minutes)

        # Текущее время
        current_time = datetime.now()

        # Время отправки сообщения
        send_time = current_time + random_time

        # Проверка, попадает ли время отправки в запрещённый временной интервал (01:00 - 07:00)
        #if send_time.time() >= datetime.strptime('01:00:00', '%H:%M:%S').time() and send_time.time() < datetime.strptime('07:00:00', '%H:%M:%S').time():
            #continue

        print(f"Следующее сообщение будет отправлено {send_time.strftime('%d.%m.%y %H:%M')}")
        # Рассчитываем задержку в секундах
        delay_seconds = delay_hours * 3600 + delay_minutes * 60
        # Ожидаем заданное время
        time.sleep(delay_seconds)

        # Чтение случайной строки из файла lines.txt
        with open('lines.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            random_line = random.choice(lines).strip()

        try:
            # Отправка сообщения пользователю
            await app.send_message(user_id, random_line)
            print(f"Отправлено сообщение: '{random_line}'")
        except Exception as e:
            print(f"Ошибка отправки сообщения: {e}")

# Запуск клиента Pyrogram и отправка сообщений
with app:
    app.loop.run_until_complete(send_random_message())