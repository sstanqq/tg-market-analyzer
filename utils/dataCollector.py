from binance.client import Client
import pandas as pd
from datetime import datetime
import time


from config import BINANCE_API, BINANCE_SEC

# Подключаем Binance api
client = Client(BINANCE_API, BINANCE_SEC)

# Получаем свечи за определенный период
def getKlines(symbol, period, startCol):
    per = Client.KLINE_INTERVAL_1HOUR
    if period == "1m":
        per = Client.KLINE_INTERVAL_1MINUTE
    elif period == "30m":
        pre = Client.KLINE_INTERVAL_30MINUTE
    elif period == "1h":
        per = Client.KLINE_INTERVAL_1HOUR
    elif period == "1d":
        per = Client.KLINE_INTERVAL_1DAY
    elif period == "1w":
        per = Client.KLINE_INTERVAL_1WEEK
    elif period == "1M":
        per = Client.KLINE_INTERVAL_1MONTH
    else:
        per = Client.KLINE_INTERVAL_1MINUTE

    # Параметры get_historical_klines:
    #   1. Символ
    #   2. Интервал между измерениями
    #   3. Интервал между началом измерений и концом
    #   4. Спото и фьючерсы

    klines = client.get_historical_klines(symbol, per, startCol)

    priceInfo = {}

    priceInfo['Time'] = []
    priceInfo['Open'] =  []
    priceInfo['Close'] = []
    priceInfo['Volume'] = []

    for kline in klines:
        date = datetime.fromtimestamp(kline[0]/1000)

        priceInfo['Time'].append(date)
        priceInfo['Open'].append(float(kline[1]))
        priceInfo['Close'].append(float(kline[4]))
        priceInfo['Volume'].append(float(kline[5]))


    return priceInfo

def getTrades(symbol):
    trades = client.get_historical_trades(symbol=symbol)

    return trades

def getkl():
    klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 hour ago UTC")

    return klines

def writeInfo(path, fName, data):
    # Получаем даты измерений
    dates = data['Time']
    openPrices = data['Open']
    closePrices = data['Close']
    volumes = data['Volume']

    with open((path + "\\"+ fName), "w") as f:
        for i in range(len(dates)):
            date = dates[i]
            openPrice = openPrices[i]
            closePrice = closePrices[i]
            volume = volumes[i]
            strDate = f"{date.day}.{date.month}.{date.year}-{date.hour}:{date.minute}"

            if i == (len(dates)-1):
                f.write(f"{strDate} {openPrice} {closePrice} {volume}")
            else:
                f.write(f"{strDate} {openPrice} {closePrice} {volume}\n")
