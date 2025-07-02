def check_stock_risk(predicted_days):
    return predicted_days < 3

def check_eta_risk(eta, threshold=60):
    return eta > threshold
