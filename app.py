# --- IT CRM Web App ---
try:
    import streamlit as st
    import pandas as pd
    import sqlite3
    from datetime import datetime
    import plotly.express as px
except ModuleNotFoundError:
    raise ModuleNotFoundError("Please install required packages: streamlit, pandas, plotly")

# ... content skipped for brevity ...
        st.plotly_chart(cat_fig, use_container_width=True)
