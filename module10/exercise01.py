import time

import requests
import schedule


def call_rest_api():
    res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    print(res.json())


schedule.every(3).seconds.do(call_rest_api)

while 1:
    schedule.run_pending()
    time.sleep(1)
