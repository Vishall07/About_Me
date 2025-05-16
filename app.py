import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Students Performance Dashboard", layout="wide")

# Load data
df = pd.read_csv("StudentPerformanceFactors.csv")

st.title("📊 Students Performance Dashboard")

# Show raw data
with st.expander("🔍 Show Raw Data"):
    st.dataframe(df.head(), use_container_width=True)

# Sidebar Filters
st.sidebar.header("🧰 Filter Options")

categorical_vars = df.select_dtypes(include="object").columns.tolist()
numerical_vars = df.select_dtypes(include="number").columns.tolist()

cat_col = st.sidebar.selectbox("Select Categorical Variable", categorical_vars)
num_col = st.sidebar.selectbox("Select Numerical Variable", numerical_vars)

# Dynamic summary
st.sidebar.markdown("### 📈 Variable Summary")
st.sidebar.write(f"**Mean of {num_col}**: {df[num_col].mean():.2f}")
st.sidebar.write(f"**Median of {num_col}**: {df[num_col].median():.2f}")
st.sidebar.write(f"**Unique in {cat_col}**: {df[cat_col].nunique()}")

# Plot section
st.subheader(f"🎯 {num_col} Distribution by {cat_col}")

# Plotly interactive boxplot
fig = px.box(df, x=cat_col, y=num_col, color=cat_col, points="all",
             title=f"{num_col} by {cat_col}",
             labels={cat_col: cat_col, num_col: num_col})

fig.update_layout(
    title_x=0.5,
    xaxis_title=cat_col,
    yaxis_title=num_col,
    boxmode='group',
    template='plotly_white',
    height=500
)

st.plotly_chart(fig, use_container_width=True)
