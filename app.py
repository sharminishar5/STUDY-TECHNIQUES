import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Scientific Visualization", layout="wide")

# Load your dataset
df = pd.read_csv("your_dataset.csv")  # replace with your CSV file name

st.title("Scientific Visualization Dashboard")

# Create 3 tabs
tab1, tab2, tab3 = st.tabs(["Stress", "Distraction", "Motivation"])

# ---------- Tab 1 ----------
with tab1:
    st.header("Page 1: Stress Levels")
    if 'Stress' in df.columns:
        st.bar_chart(df['Stress'])
    else:
        st.write("No 'Stress' column in dataset")

# ---------- Tab 2 ----------
with tab2:
    st.header("Page 2: Distraction Levels")
    if 'Distraction' in df.columns:
        st.line_chart(df['Distraction'])
    else:
        st.write("No 'Distraction' column in dataset")

# ---------- Tab 3 ----------
with tab3:
    st.header("Page 3: Motivation Levels")
    if 'Motivation' in df.columns:
        st.area_chart(df['Motivation'])
    else:
        st.write("No 'Motivation' column in dataset")
