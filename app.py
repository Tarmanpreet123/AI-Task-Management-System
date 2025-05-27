import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Task & User Dashboard", layout="wide")

# Title
st.title("📊 Synthetic Task and User Profile Dashboard")

# Sidebar options
st.sidebar.header("📁 Upload Your CSV Files")

# Upload CSV files
task_file = st.sidebar.file_uploader("Upload Task Data CSV", type="csv")
user_file = st.sidebar.file_uploader("Upload User Profile CSV", type="csv")

# Load data if files are provided
if task_file and user_file:
    task_df = pd.read_csv(task_file)
    user_df = pd.read_csv(user_file)

    st.subheader("🗂 Task Data")
    with st.expander("View Task Dataset"):
        st.dataframe(task_df)

    st.subheader("👤 User Profiles")
    with st.expander("View User Dataset"):
        st.dataframe(user_df)

    # Filter task data
    st.sidebar.header("🔎 Filter Tasks")
    selected_user = st.sidebar.selectbox("Assigned To", ["All"] + sorted(task_df["Assigned_To"].unique().tolist()))
    selected_category = st.sidebar.multiselect("Category", task_df["Category"].unique())
    selected_priority = st.sidebar.multiselect("Priority", task_df["Priority"].unique())

    filtered_df = task_df.copy()
    if selected_user != "All":
        filtered_df = filtered_df[filtered_df["Assigned_To"] == selected_user]
    if selected_category:
        filtered_df = filtered_df[filtered_df["Category"].isin(selected_category)]
    if selected_priority:
        filtered_df = filtered_df[filtered_df["Priority"].isin(selected_priority)]

    st.subheader("📋 Filtered Tasks")
    st.write(f"Showing {len(filtered_df)} tasks")
    st.dataframe(filtered_df)

    # Visualizations
    st.subheader("📈 Task Distribution by Category")
    fig1, ax1 = plt.subplots()
    task_df["Category"].value_counts().plot(kind="bar", ax=ax1, color="skyblue")
    st.pyplot(fig1)

    st.subheader("🏅 User Performance Overview")
    fig2, ax2 = plt.subplots()
    user_df.plot(kind='bar', x='User_ID', y='Performance_Score', ax=ax2, color='green')
    st.pyplot(fig2)

else:
    st.info("📂 Please upload both the task and user CSV files to begin.")

