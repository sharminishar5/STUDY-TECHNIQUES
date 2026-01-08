import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Stress & Motivation", layout="wide")

st.title("Page 2: Stress, Distraction & Motivation")
st.write(
    "This page analyses how stress, distraction, and motivation affect students’ learning habits."
)

@st.cache_data
def load_data():
    return pd.read_csv("cleaned_student_study_dataset_FINAL.csv")

df = load_data()

st.subheader("1. Average Stress, Distraction and Motivation")

avg_challenges = df[['obs_time', 'obs_distraction', 'obs_motivation']].mean()

fig, ax = plt.subplots(figsize=(8,5))
ax.bar(
    ['Stress', 'Distraction', 'Lack of Motivation'],
    avg_challenges.values
)

ax.set_title("Average Stress, Distraction and Motivation Challenges")
ax.set_ylabel("Average Challenge Level")
ax.set_xlabel("Type of Challenge")

st.pyplot(fig)

st.subheader("2. Correlation Heatmap")

df_heatmap = df[['obs_time', 'obs_distraction', 'Motivation']].copy()
df_heatmap = df_heatmap.rename(columns={
    'obs_time': 'Stress',
    'obs_distraction': 'Distraction'
})

fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(
    df_heatmap.corr(),
    annot=True,
    ax=ax
)

ax.set_title("Correlation Between Stress, Distraction and Motivation")
st.pyplot(fig)

st.subheader("3. Relationship Between Stress and Motivation")

fig, ax = plt.subplots(figsize=(8,5))
ax.scatter(
    df['obs_time'],
    df['Motivation']
)

ax.set_xlabel("Stress Level (Lack of Time)")
ax.set_ylabel("Motivation")
ax.set_title("Stress vs Motivation")

st.pyplot(fig)

st.subheader("4. Motivation Across Distraction Levels")

fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(
    data=df,
    x='obs_distraction',
    y='Motivation',
    ax=ax
)

ax.set_xlabel("Distraction Level (Phone / Social Media)")
ax.set_ylabel("Motivation")
ax.set_title("Motivation Across Different Distraction Levels")

st.pyplot(fig)

st.subheader("5. Motivation Trend Across Stress Levels")

stress_motivation = df.groupby('obs_time')['obs_motivation'].mean()

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(
    stress_motivation.index,
    stress_motivation.values,
    marker='o'
)

ax.set_title("Motivation Challenge Across Increasing Stress Levels")
ax.set_xlabel("Stress Level")
ax.set_ylabel("Average Lack of Motivation")

st.pyplot(fig)

