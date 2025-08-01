from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def launch_browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get("https://app.eobroker.com/trade/smarty")
    time.sleep(10)
    candles = driver.execute_script("return [...document.querySelectorAll('.chart-candlestick')].map(c => c.getAttribute('d'))")
    driver.quit()
    return candles