# IT CRM Dashboard

## Overview
This web app is built using Streamlit and provides a centralized dashboard for managing IT tasks and tickets.

## Users
- **IT Admin (Prakash Darekar)**: Can create/edit/assign tasks, update statuses, and view analytics.
- **IT Staff (Kiran, Durgesh, Abhishek, Samadhan)**: Can submit task requests.

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the app:
```
streamlit run app.py
```

## Features
- Role-based login
- Ticket creation by IT staff and admin
- Admin task assignment
- Auto-generated task numbers
- Visualization via bar and pie charts
- SQLite database storage

**Note**: No email integration included.

## File Structure
- `app.py`: Main app script
- `requirements.txt`: Python dependencies
- `README.md`: App documentation
- `it_crm.db`: Database (auto-created on first run)

---

Developed with ❤️ in Streamlit
