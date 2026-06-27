# app.py
import streamlit as st
import pandas as pd
import loan_manage_01

st.set_page_config(layout="wide", page_title="SHG Ledger")

# --- Physical-register look & feel (self-contained "paper card" so it
#     stays readable in both light and dark Streamlit themes) ---
st.markdown(
    """
    <style>
    .ledger-card {
        background-color: #f8f4ea;
        border: 1px solid #d9d2bd;
        border-radius: 10px;
        padding: 18px 22px;
        margin-bottom: 18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    .ledger-title {
        text-align: center;
        font-family: 'Courier New', monospace;
        font-size: 28px;
        font-weight: 700;
        color: #3a4a45;
        border-bottom: 3px double #b9ad8d;
        padding-bottom: 8px;
        margin-bottom: 6px;
    }
    .ledger-subtitle {
        text-align: center;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        color: #6b6356;
        margin: 0;
    }
    .section-head {
        font-family: 'Courier New', monospace;
        font-size: 17px;
        font-weight: 700;
        color: #2f4a3c;
        background-color: #d9e7dc;
        border: 1px solid #b7cdbb;
        border-radius: 6px;
        padding: 6px 10px;
        text-align: center;
        margin-bottom: 10px;
    }
    .ledger-table table {
        font-family: 'Courier New', monospace !important;
        border-collapse: collapse;
        width: 100%;
    }
    .ledger-table th, .ledger-table td {
        border: 1px solid #d9d2bd !important;
        text-align: center !important;
        padding: 8px !important;
        color: #33392f !important;
        background-color: #fdfbf6 !important;
    }
    .ledger-table th {
        background-color: #ece6d4 !important;
        font-weight: 700;
    }
    .next-principal-box {
        font-family: 'Courier New', monospace;
        font-size: 16px;
        color: #2f4a3c;
        text-align: center;
        background-color: #e3edd8;
        border: 2px dashed #8fae8a;
        border-radius: 8px;
        padding: 12px;
        margin-top: 4px;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="ledger-card">'
    '<div class="ledger-title">📒 SHG LOAN REGISTER</div>'
    '<div class="ledger-subtitle">Monthly Demand &amp; Collection Ledger</div>'
    '</div>',
    unsafe_allow_html=True,
)

# --- Inputs ---
col_in1, col_in2, col_in3 = st.columns(3)

with col_in1:
    principal = st.number_input("1. Principal Amount (Rs.):", min_value=0.0, value=200000.0, step=1000.0)

with col_in2:
    monthly_rate = st.number_input("2. Monthly Interest Rate (%):", min_value=0.0, value=1.0, step=0.1)

with col_in3:
    collection_total = st.number_input("3. Collection Total (This Month, Rs.):", min_value=0.0, value=20000.0, step=500.0)

# --- Calculation ---
demand_data, collection_data, next_principal = loan_manage_01.calculate_ledger(
    principal=principal,
    monthly_rate=monthly_rate,
    collection_total=collection_total,
)

st.write("")

demand_html = pd.DataFrame(demand_data).to_html(index=False)
collection_html = pd.DataFrame(collection_data).to_html(index=False)

# --- Output Tables (built as one HTML block so the card nests correctly) ---
st.markdown(
    f"""
    <div class="ledger-card">
        <div style="display:flex; gap:20px; flex-wrap:wrap;">
            <div style="flex:1; min-width:260px;">
                <div class="section-head">DEMAND (Due This Month)</div>
                <div class="ledger-table">{demand_html}</div>
            </div>
            <div style="flex:1; min-width:260px;">
                <div class="section-head">COLLECTION (Received This Month)</div>
                <div class="ledger-table">{collection_html}</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Next Principal Balance ---
st.markdown(
    f'<div class="next-principal-box">📌 NEXT MONTH\'S OPENING PRINCIPAL: Rs. {next_principal:.2f}</div>',
    unsafe_allow_html=True,
)