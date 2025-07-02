import pandas as pd
from sklearn.linear_model import LinearRegression

def train_eta_model(df):
    features = df[['Distance_km', 'Traffic_delay', 'Weather_severity']]
    target = df['Actual_delivery_time_min']
    model = LinearRegression()
    model.fit(features, target)
    return model

def predict_eta(model, dist, delay, weather):
    return model.predict([[dist, delay, weather]])[0]
