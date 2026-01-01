import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Scientific Visualization", layout="wide")

# Load dataset
df = pd.read_csv("your_dataset.csv")  # replace with your file name

# Sidebar navigation
page = st.sidebar.radio("Select Page", ["Page 1", "Page 2", "Page 3"])

if page == "Page 1":
    st.title("Page 1: Stress")
    if 'Stress' in df.columns:
        st.bar_chart(df['Stress'])
    else:
        st.write("No Stress column found")

elif page == "Page 2":
    st.title("Page 2: Distraction")
    if 'Distraction' in df.columns:
        st.bar_chart(df['Distraction'])
    else:
        st.write("No Distraction column found")

elif page == "Page 3":
    st.title("Page 3: Motivation")
    if 'Motivation' in df.columns:
        st.bar_chart(df['Motivation'])
    else:
        st.write("No Motivation column found")
