# --- IT CRM Web App ---
try:
    import streamlit as st
    import pandas as pd
    import sqlite3
    from datetime import datetime
    import plotly.express as px
except ModuleNotFoundError:
    raise ModuleNotFoundError("Please install required packages: streamlit, pandas, plotly")

# --- Database Setup ---
conn = sqlite3.connect("it_crm.db", check_same_thread=False)
c = conn.cursor()

# Task Log Table
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
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
)""")
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

def update_status(task_id, new_status):
    c.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()

# --- Streamlit UI ---
st.set_page_config(page_title="IT DEPARTMENT DASHBOARD", layout="wide")
st.title("💻 IT DEPARTMENT DASHBOARD")

# --- Authentication ---
user_type = st.sidebar.selectbox("Login as", ["IT Admin", "IT Staff"])

staff_names = ["KIRAN KULKARNI", "DURGESH SHARMA", "ABHISHEK JADHAV", "SAMADHAN BURKUL"]
statuses = ["Open", "In Progress", "Closed"]

# --- Task Entry Form ---
def task_entry_form():
    with st.form("task_form"):
        plant = st.text_input("Plant", value="Plant A")
        raised_by = st.text_input("Raised By")
        raised_date = st.date_input("Raised Date")
        completion_date = st.date_input("Completion Date")
        department = st.text_input("Department", value="Production")
        category = st.text_input("Category", value="Hardware")
        sub_category = st.text_input("Sub-Category", value="Printer")
        task = st.text_input("Task Title")
        description = st.text_area("Task Description")
        start_date = st.date_input("Start Date")
        promise_date = st.date_input("Promise Date")
        status = st.selectbox("Status", statuses)
        remark = st.text_area("Remarks")
        submit = st.form_submit_button("Submit Task")

        if submit:
            task_no = generate_task_no()
            task_data = (
                task_no, plant, raised_by, raised_date.strftime('%Y-%m-%d'),
                completion_date.strftime('%Y-%m-%d'), department, category,
                sub_category, task, description, start_date.strftime('%Y-%m-%d'),
                promise_date.strftime('%Y-%m-%d'), status, remark, ""
            )
            add_task(task_data)
            st.success(f"Task {task_no} submitted successfully!")

# --- IT Staff View ---
if user_type == "IT Staff":
    st.subheader("📝 Generate IT Task Request")
    task_entry_form()

# --- IT Admin View ---
elif user_type == "IT Admin":
    st.subheader("👨‍💼 Welcome IT Admin: PRAKASH DAREKAR")

    st.markdown("### 📝 Create New Task")
    task_entry_form()

    df = get_all_tasks()
    if df.empty:
        st.warning("No tasks have been submitted yet.")
    else:
        st.markdown("### 📋 All Task Logs")
        st.dataframe(df.sort_values(by="raised_date", ascending=False), use_container_width=True)

        st.markdown("### 🧑‍🏫 Assign Tasks to IT Staff")
        with st.form("assign_form"):
            task_ids = df["id"].tolist()
            task_to_assign = st.selectbox("Select Task ID to Assign", task_ids)
            assign_person = st.selectbox("Assign To", staff_names)
            if st.form_submit_button("Assign Task"):
                update_assignment(task_to_assign, assign_person)
                st.success(f"Task ID {task_to_assign} assigned to {assign_person}")

        st.markdown("### 🔁 Update Task Status")
        with st.form("status_form"):
            task_to_update = st.selectbox("Select Task ID to Update Status", task_ids, key="status_update")
            new_status = st.selectbox("New Status", statuses)
            if st.form_submit_button("Update Status"):
                update_status(task_to_update, new_status)
                st.success(f"Status of Task ID {task_to_update} updated to {new_status}")

        st.markdown("### 📊 Task Distribution by Status")
        status_fig = px.bar(df, x="status", title="Task Count by Status", color="status")
        st.plotly_chart(status_fig, use_container_width=True)

        st.markdown("### 🥧 Task Distribution by Category")
        cat_fig = px.pie(df, names="category", title="Tasks by Category")
        st.plotly_chart(cat_fig, use_container_width=True)
