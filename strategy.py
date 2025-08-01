def analyze_candles(candles):
    if not candles or len(candles) < 5:
        return "🚫 لا توجد بيانات كافية"
    green = sum(1 for c in candles[-5:] if 'green' in c)
    red = sum(1 for c in candles[-5:] if 'red' in c)
    if green > red:
        return "📈 شراء (Buy)"
    else:
        return "📉 بيع (Sell)"