import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

# Custom CSS for light blue theme
st.markdown("""
    <style>

        .sub-title {
            font-size: 16px;
            color: #90e0ef;
            margin-bottom: 1.5rem;
        }

        /* Expense form container */
        .expense-form {
            background-color: #ADE8F4;;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            margin-bottom: 20px;
        }

        .form-header {
            font-weight: 600;
            color: #ADE8F4;
            font-size: 15px;
        }

        /* Override primary button */
        button[kind="primary"] {
            background-color: #3498DB !important;
            color: white !important;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5rem 1.5rem;
        }

        /* Input label color override */
        label {
            color: #34495E !important;
        }
    </style>
""", unsafe_allow_html=True)


def add_update_tab():

    selected_date = st.date_input(
        "Enter Date",
        datetime(2025, 6, 21),
        label_visibility="collapsed"
    )

    # Fetch existing expenses
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("❌ Failed to retrieve expenses.")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        # st.markdown('<div class="expense-form">', unsafe_allow_html=True)

        # Table headers
        header1, header2, header3 = st.columns(3)
        with header1: st.markdown('<div class="form-header">💵 Amount</div>', unsafe_allow_html=True)
        with header2: st.markdown('<div class="form-header">📂 Category</div>', unsafe_allow_html=True)
        with header3: st.markdown('<div class="form-header">📝 Notes</div>', unsafe_allow_html=True)

        expenses = []

        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=amount,
                    key=f"amount_{i}",
                    format="%.2f",
                    label_visibility="collapsed"
                )
            with col2:
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    index=categories.index(category),
                    key=f"category_{i}",
                    label_visibility="collapsed"
                )
            with col3:
                notes_input = st.text_input(
                    label="Notes",
                    value=notes,
                    key=f"notes_{i}",
                    label_visibility="collapsed",
                    placeholder="Optional notes..."
                )

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button("💾 Save Expenses")
        st.markdown('</div>', unsafe_allow_html=True)

        if submit_button:
            filtered_expenses = [e for e in expenses if e['amount'] > 0]
            if not filtered_expenses:
                st.warning("⚠️ Please enter at least one expense with an amount greater than 0.")
            else:
                response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
                if response.status_code == 200:
                    st.success("✅ Expenses updated successfully!")
                else:
                    st.error("❌ Failed to update expenses.")
