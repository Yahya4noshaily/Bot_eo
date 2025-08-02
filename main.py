from strategies.macd_rsi_combo import analyze_macd_rsi
from strategies.support_resistance import check_support_resistance
from filters import is_volatile
import json

with open("config.json") as f:
    config = json.load(f)

price = 1.23  # مثال تمثيلي
if not is_volatile(price):
    if analyze_macd_rsi(price) and check_support_resistance(price):
        print("✅ دخول آمن")
    else:
        print("⏳ انتظار")