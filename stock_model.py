import pandas as pd
from sklearn.linear_model import LinearRegression

def train_stock_model(df):
    df = df.copy()

    # Feature engineering
    df['Rolling_Sales'] = df['Units_Sold'].rolling(window=3).mean()

    # Replace or fill invalid values
    df['Rolling_Sales'] = df['Rolling_Sales'].fillna(0.1)
    df['Inventory_Level'] = df['Inventory_Level'].replace(0, 0.1)
    df['Days_Until_Stockout'] = df['Inventory_Level'] / df['Rolling_Sales']

    # Drop or fix inf/NaN rows
    df = df.replace([float('inf'), -float('inf')], pd.NA).dropna()

    features = df[['Rolling_Sales', 'Inventory_Level']]
    target = df['Days_Until_Stockout']

    model = LinearRegression()
    model.fit(features, target)
    return model


def predict_stockout(model, rolling_sales, inventory_level):
    input_df = pd.DataFrame([[rolling_sales, inventory_level]], columns=['Rolling_Sales', 'Inventory_Level'])
    prediction = model.predict(input_df)
    return prediction[0]