import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from monthly_analytics_ui import monthly_analytics_tab
st.markdown("""
    <style>
        /* Main title */
        .main-title {
            font-size: 42px;
            font-weight: 700;
            color: #ADE8F4;
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)
# st.title("Expense Tracking System")
st.markdown('<div class="main-title">💸 Expense Tracking System</div>', unsafe_allow_html=True)
tab1, tab2,tab3 = st.tabs(["Add/Update", "Analytics By Category","Analytics By Months"])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()

with tab3:
    monthly_analytics_tab()
