import streamlit as st
import requests
import pandas as pd
import altair as alt

API_URL = "http://localhost:8000"

def monthly_analytics_tab():
    response = requests.get(f"{API_URL}/monthly-analytics/")

    if response.status_code != 200:
        st.error(f"Error fetching data: {response.status_code}")
        st.text(response.text)
        return

    monthly_summary = response.json()

    df = pd.DataFrame(monthly_summary)

    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    }, inplace=True)

    df_sorted = df.sort_values(by="Month Number")

    # st.markdown(
    #     "<h3 style='color: teal; font-weight: 600;'>Expense Breakdown By Months</h3>",
    #     unsafe_allow_html=True
    # )

    chart = alt.Chart(df_sorted).mark_bar().encode(
        x=alt.X('Month Name:N', sort=None, axis=alt.Axis(labelAngle=-45, title=None)),
        y=alt.Y('Total:Q', axis=alt.Axis(title=None))
    ).properties(
        width='container',
        height=400
    )
    st.altair_chart(chart, use_container_width=True)

    df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

    st.table(df_sorted[["Month Name", "Total"]])
