import streamlit as st
import pandas as pd
from stock_model import train_stock_model, predict_stockout
from delivery_model import train_eta_model, predict_eta
from utils.data_loader import load_inventory_data, load_delivery_data
from utils.alerts import check_stock_risk, check_eta_risk

st.set_page_config(layout="wide")
st.sidebar.title("RetailOptimizer")
page = st.sidebar.selectbox("Choose Page", ["Inventory Monitor", "Delivery Optimizer"])

if page == "Inventory Monitor":
    st.title("📦 Inventory & Stockout Predictor")
    df = load_inventory_data()
    model = train_stock_model(df)

    st.dataframe(df.tail())
    inventory = st.slider("Current Inventory", 0, 100, 30)
    sales_rate = st.slider("Avg Daily Sales", 1, 20, 5)

    predicted_days = predict_stockout(model, inventory, sales_rate)
    st.metric("Predicted Days Until Stockout", f"{predicted_days:.2f}")

    if check_stock_risk(predicted_days):
        st.warning("⚠️ Risk of stockout in next 3 days!")

elif page == "Delivery Optimizer":
    st.title("🚚 Delivery ETA Predictor")
    dist = st.slider("Distance (km)", 1, 50, 20)
    traffic = st.slider("Traffic Delay (min)", 0, 30, 10)
    weather = st.slider("Weather Severity (0-5)", 0, 5, 1)

    sample_df = pd.DataFrame({
        "Distance_km": [20, 25, 15],
        "Traffic_delay": [5, 10, 7],
        "Weather_severity": [1, 2, 0],
        "Actual_delivery_time_min": [45, 55, 40]
    })

    model = train_eta_model(sample_df)
    eta = predict_eta(model, dist, traffic, weather)

    st.metric("Estimated Arrival Time (min)", f"{eta:.1f}")
    if check_eta_risk(eta):
        st.warning("⚠️ Delivery may be delayed!")
