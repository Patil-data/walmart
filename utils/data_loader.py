import pandas as pd
import json

def load_inventory_data(path="data/inventory_data.csv"):
    try:
        df = pd.read_csv(path)

        # Drop rows with missing critical values
        df = df.dropna(subset=['Units_Sold', 'Inventory_Level'])

        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Inventory file not found at: {path}")
    except Exception as e:
        raise RuntimeError(f"Error loading inventory data: {e}")

def load_delivery_data(path="data/delivery_data.json"):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        return pd.DataFrame(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Delivery file not found at: {path}")
    except Exception as e:
        raise RuntimeError(f"Error loading delivery data: {e}")
