def analyze_macd_rsi(price):
    if price < 1.2:
        return True  # دخول شراء
    elif price > 1.3:
        return True  # دخول بيع
    return False