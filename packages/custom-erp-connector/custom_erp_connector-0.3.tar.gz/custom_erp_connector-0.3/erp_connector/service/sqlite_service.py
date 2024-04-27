import sqlite3
from datetime import datetime, timedelta


def create_table():
    conn = sqlite3.connect('scheduler_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scheduler_data
                 (id INTEGER PRIMARY KEY,
                 started_at TEXT,
                 updated_at TEXT,
                 command TEXT,
                 command_id TEXT,
                 status TEXT)''')
    conn.commit()
    conn.close()


def insert_data():
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('scheduler_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO scheduler_data (started_at,updated_at) VALUES (?, ?)",
              (start_time, start_time))
    conn.commit()
    row_id = c.lastrowid
    conn.close()
    return row_id


def update_data(row_id, command,command_id, status):
    conn = sqlite3.connect('scheduler_data.db')
    updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c = conn.cursor()
    c.execute("UPDATE scheduler_data SET updated_at = ?, command = ?, command_id = ?, status = ? WHERE id = ?",
              (updated_at, command,command_id, status, row_id))
    conn.commit()
    conn.close()


def delete_old_records():
    conn = sqlite3.connect('scheduler_data.db')
    c = conn.cursor()
    one_month_ago = datetime.now() - timedelta(days=30)
    c.execute("DELETE FROM scheduler_data WHERE start_time < ?", (one_month_ago,))
    conn.commit()
    conn.close()
