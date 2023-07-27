import base
import reminder

if __name__ == "__main__":
    base.create_clients_table()
    reminder.send_reminders()
