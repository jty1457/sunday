import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 시계열데이터 주식거래량, 일별날씨변동, bike따릉이 경험
# ts = pd.date_range(1start, 2end, 3periods갯수, 4freq월별일, 5tz타임존)

print("ts2 periods=24, freq='3MS'")
ts1 = pd.date_range(
     start='2022-01-01', end=None, periods=12, freq='3MS', tz='Asia/Seoul'
    )
print(ts1)
print()

print("ts2 periods=24, freq='M'")
ts2 = pd.date_range(
     start='2022-01-01', end=None, periods=12, freq='M', tz='Asia/Seoul'
    )
print(ts2)
print()

print("ts3 periods=24, freq='MS'")
ts3 = pd.date_range(
     start='2022-01-01', end=None, periods=12, freq='MS', tz='Asia/Seoul'
    )
print(ts3)
print()


print("ts4 periods=6, freq='2H' ")
ts4 = pd.date_range(
     start='2022-01-01', end=None, periods=36, freq='2H', tz='Asia/Seoul'
    )
print(ts4)
print()


























print()
print()