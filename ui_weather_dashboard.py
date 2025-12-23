import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Advanced Weather Dashboard", layout="wide")

# Load data
data = pd.read_csv("weather.csv")

# Sidebar
st.sidebar.title("🌍 Weather Dashboard")
city = st.sidebar.selectbox("Select City", data["City"].unique())
city_data = data[data["City"] == city].iloc[0]

# Title
st.title("🌦️ Advanced Weather Monitoring Dashboard")
st.markdown("UI-based weather analysis using Python & Streamlit")

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Analysis", "📄 Dataset"])

# -------- TAB 1 : OVERVIEW --------
with tab1:
    st.subheader(f"📍 Weather in {city}")

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("🌡️ Temp (°C)", city_data["Temperature"])
    c2.metric("💧 Humidity (%)", city_data["Humidity"])
    c3.metric("💨 Wind (km/h)", city_data["WindSpeed"])
    c4.metric("🌧️ Rain (mm)", city_data["Rainfall"])
    c5.metric("☀️ UV Index", city_data["UV_Index"])

    st.divider()

    st.write(f"🌍 **Air Quality:** {city_data['AirQuality']}")
    st.write(f"🧭 **Pressure:** {city_data['Pressure']} hPa")
    st.write(f"👁️ **Visibility:** {city_data['Visibility']} km")

    st.subheader("🧠 Weather Insight")
    if city_data["Temperature"] > 32:
        st.write("🔥 Hot weather – stay hydrated.")
    elif city_data["Temperature"] < 20:
        st.write("❄️ Cool weather – wear warm clothes.")
    else:
        st.write("🌤️ Pleasant weather conditions.")

# -------- TAB 2 : ANALYSIS --------
with tab2:
    st.subheader("📊 City-wise Comparison")

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        ax1.bar(data["City"], data["Temperature"])
        ax1.set_title("Temperature Comparison (°C)")
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots()
        ax2.bar(data["City"], data["Rainfall"])
        ax2.set_title("Rainfall Comparison (mm)")
        st.pyplot(fig2)

    st.subheader("📈 Temperature vs Humidity Trend")
    fig3, ax3 = plt.subplots()
    ax3.plot(data["City"], data["Temperature"], marker='o', label="Temperature")
    ax3.plot(data["City"], data["Humidity"], marker='s', label="Humidity")
    ax3.legend()
    st.pyplot(fig3)

# -------- TAB 3 : DATASET --------
with tab3:
    st.subheader("📄 Complete Dataset")
    st.dataframe(data)
    st.write("📌 Dataset Statistics")
    st.write(data.describe())
