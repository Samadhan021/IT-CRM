
# IT CRM Web App

This is a simple IT CRM Dashboard for the IT Department.

## Features

- Only IT Staff can generate tickets
- IT Admin (PRAKASH DAREKAR) can:
  - View all submitted tasks
  - Assign tasks to IT Staff
  - Update task statuses
  - View analytics via bar and pie charts

## Staff Members

- KIRAN KULKARNI
- DURGESH SHARMA
- ABHISHEK JADHAV
- SAMADHAN BURKUL

## Technologies Used

- Streamlit
- SQLite
- Pandas
- Plotly

## How to Run

1. Make sure you have Python installed (version 3.7 or higher).
2. Install the required Python packages:

```bash
pip install streamlit pandas plotly
```

3. Run the app using Streamlit:

```bash
streamlit run app.py
```

This will open the dashboard in your browser.

## Notes

- All task data is stored in a local SQLite database file: `it_crm.db`
- You can extend the system for authentication or export functionality if needed
