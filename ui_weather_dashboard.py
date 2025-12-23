import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Weather Dashboard", layout="wide")

# Load data
data = pd.read_csv("weather.csv")

# Sidebar UI
st.sidebar.title("🌍 Weather Dashboard")
city = st.sidebar.selectbox("Select City", data["City"].unique())

# Filter data
city_data = data[data["City"] == city].iloc[0]

# Main Title
st.title("🌦️ Weather Monitoring Dashboard")
st.markdown(f"### 📍 City: **{city}**")

# Metrics UI
col1, col2, col3, col4 = st.columns(4)

col1.metric("🌡️ Temperature (°C)", city_data["Temperature"])
col2.metric("💧 Humidity (%)", city_data["Humidity"])
col3.metric("💨 Wind Speed (km/h)", city_data["WindSpeed"])
col4.metric("🌧️ Rainfall (mm)", city_data["Rainfall"])

st.divider()

# Charts Section
st.subheader("📊 Weather Comparison Across Cities")

col5, col6 = st.columns(2)

# Temperature Bar Chart
with col5:
    fig1, ax1 = plt.subplots()
    ax1.bar(data["City"], data["Temperature"])
    ax1.set_title("Temperature Comparison")
    ax1.set_ylabel("°C")
    st.pyplot(fig1)

# Rainfall Bar Chart
with col6:
    fig2, ax2 = plt.subplots()
    ax2.bar(data["City"], data["Rainfall"])
    ax2.set_title("Rainfall Comparison")
    ax2.set_ylabel("mm")
    st.pyplot(fig2)

st.divider()

# Dataset view
with st.expander("📄 View Complete Dataset"):
    st.dataframe(data)
