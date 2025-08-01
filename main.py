from browser import launch_browser
from strategy import analyze_candles

if __name__ == "__main__":
    candles = launch_browser()
    signal = analyze_candles(candles)
    print("✅ توصية:", signal)