# 📘 IT CRM Web App – README

## 🔰 Overview
The **IT DEPARTMENT DASHBOARD** is a web-based CRM system built in **Python + Streamlit + SQLite**. It helps the IT Admin manage and assign tickets to staff. IT Staff can raise task requests, and the Admin can view, assign, update, and monitor all tasks.

## 🧑‍💻 Roles

- 👨‍💼 **IT Admin:** `PRAKASH DAREKAR` (Full Access)
- 👨‍🔧 **IT Staff:**
  - KIRAN KULKARNI
  - DURGESH SHARMA
  - ABHISHEK JADHAV
  - SAMADHAN BURKUL

## ⚙️ Features

- Create task tickets (both Admin & Staff)
- Assign tasks to IT Staff
- Auto-generate task number
- Notifications logged for assignments
- Status updates
- Dropdowns for Plant, Department, Category, etc.
- Dashboard with bar and pie charts
- Task form does **not refresh** after submission
- SQLite-backed persistent data
- 🎯 Admin-only data visibility

## 🗃️ Folder Structure

```
it-crm/
├── app.py                  # Main Streamlit App
├── it_crm.db               # SQLite3 database (auto-created)
├── README.md               # You're reading it
├── requirements.txt        # Python dependencies
```

## ▶️ How to Run

1. 📦 **Install requirements**
```
pip install -r requirements.txt
```

2. 🚀 **Run the app**
```
streamlit run app.py
```

3. 🌐 Open your browser:
```
http://localhost:8501
```

## 📦 Requirements

```
streamlit
pandas
plotly
```

## 🔒 Authentication

Use the sidebar to select your role:

- `IT Admin` – Full dashboard access
- `IT Staff` – Can only submit task requests

## ❌ Email Feature

> This app intentionally **does not** include email notifications.
