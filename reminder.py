import mysql.connector
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

def get_clients_to_remind():
    today = datetime.today()
    one_month_from_today = today + timedelta(days=30)

    try:
        db_connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='ivan',
            password='3853',
            database='online_store'
        )
        cursor = db_connection.cursor()

        query = f"SELECT Name, Email, Expiry_Date FROM clients WHERE Expiry_Date <= '{one_month_from_today}'"
        cursor.execute(query)
        clients_to_remind = cursor.fetchall()

        cursor.close()
        db_connection.close()
        return clients_to_remind
    except mysql.connector.Error as err:
        print(f"Error fetching clients data: {err}")
        return []

def send_reminder_email(client):
    name, email, expiry_date = client

    subject = "Reminder: Card Expiry Date"
    body = f"Доброго дня уважаемый/ая {name}! Спешим напомнить, что срок действия вашей банковской карты истекает {expiry_date}. С уважением - Ваш онлайн-магазин"

    try:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login('dosegaev@mail.ru', 'iFRVrmXBU5v59CtzAHHG')
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = 'dosegaev@mail.ru'
        msg['To'] = email
        server.sendmail('dosegaev@mail.ru', email, msg.as_string())
        server.quit()
        print(f"Reminder email sent to {name}")
    except Exception as e:
        print(f"Error sending email to {name}: {e}")

def send_reminders():
    clients_to_remind = get_clients_to_remind()
    for client in clients_to_remind:
        send_reminder_email(client)

if __name__ == "__main__":
    send_reminders()