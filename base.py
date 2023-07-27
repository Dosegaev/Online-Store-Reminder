import mysql.connector
from datetime import datetime, timedelta
import random

def create_clients_table():
    try:
        db_connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='ivan',
            password='3853',
            database='online_store'
        )
        cursor = db_connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS clients")
        cursor.execute("""
            CREATE TABLE clients (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(100),
                Email VARCHAR(100),
                Expiry_Date DATE
            )
        """)

        today = datetime.today()
        one_month_from_today = today + timedelta(days=30)

        # Указываем фиксированный адрес электронной почты для всех клиентов
        email = 'dosegaev@mail.ru'

        for _ in range(10):
            name = f"Клиент_{random.randint(1, 100)}"  # Генерируем случайное имя для каждого клиента
            expiry_date = today + timedelta(days=random.randint(1, 30))  # Задаем случайную дату истечения срока действия карты в пределах одного месяца
            cursor.execute("INSERT INTO clients (Name, Email, Expiry_Date) VALUES (%s, %s, %s)", (name, email, expiry_date))

        db_connection.commit()
        cursor.close()
        db_connection.close()
        print("Таблица клиентов успешно создана")
    except mysql.connector.Error as err:
        print(f"Ошибка при создании таблицы клиентов: {err}")

if __name__ == "__main__":
    create_clients_table()
