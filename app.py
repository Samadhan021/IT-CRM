
# --- IT CRM Web App ---
try:
    import streamlit as st
    import pandas as pd
    import sqlite3
    from datetime import datetime
    import plotly.express as px
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("Please install required packages: streamlit, pandas, plotly") from e

# --- Database Setup ---
conn = sqlite3.connect("it_crm.db", check_same_thread=False)
c = conn.cursor()

# Task Log Table
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_no TEXT,
    plant TEXT,
    raised_by TEXT,
    raised_date TEXT,
    completion_date TEXT,
    department TEXT,
    category TEXT,
    sub_category TEXT,
    task TEXT,
    description TEXT,
    start_date TEXT,
    promise_date TEXT,
    status TEXT,
    remark TEXT,
    assigned_to TEXT
)''')
conn.commit()

# Notification Log Table
c.execute('''CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER,
    message TEXT,
    recipient TEXT,
    timestamp TEXT
)''')
conn.commit()

# --- Helper Functions ---
def generate_task_no():
    return f"TASK-{datetime.now().strftime('%Y%m%d%H%M%S')}"

def add_task(data):
    c.execute("""INSERT INTO tasks (
        task_no, plant, raised_by, raised_date, completion_date, department, category,
        sub_category, task, description, start_date, promise_date, status, remark, assigned_to
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)
    conn.commit()

def get_all_tasks():
    return pd.read_sql_query("SELECT * FROM tasks", conn)

def update_assignment(task_id, assigned_to):
    c.execute("UPDATE tasks SET assigned_to = ? WHERE id = ?", (assigned_to, task_id))
    conn.commit()
    add_notification(task_id, f"You have been assigned Task ID {task_id}", assigned_to)

def update_status(task_id, new_status):
    c.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()

def edit_task(task_id, column, new_value):
    c.execute(f"UPDATE tasks SET {column} = ? WHERE id = ?", (new_value, task_id))
    conn.commit()

def add_notification(task_id, message, recipient):
    c.execute("INSERT INTO notifications (task_id, message, recipient, timestamp) VALUES (?, ?, ?, ?)",
              (task_id, message, recipient, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()

def get_notifications_for_user(user):
    return pd.read_sql_query("SELECT * FROM notifications WHERE recipient = ? ORDER BY timestamp DESC", conn, params=(user,))

# UI & interaction left out intentionally for brevity
