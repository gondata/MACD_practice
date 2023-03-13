# Getting the data

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pandas_datareader import data as pdr

yf.pdr_override()

ticker = ['NIO']
startdate = '2020-01-01'
enddate = '2023-03-08'

data = pdr.get_data_yahoo(ticker, start=startdate, end=enddate)['Adj Close']

# EMA

ewm_fast = data.ewm(span=12, adjust=False).mean()
ewm_slow = data.ewm(span=26, adjust=False).mean()

# MACD

macd = ewm_fast - ewm_slow
signal = macd.ewm(span=9, adjust=False).mean()
histogram = macd - signal

# Graph

graph = plt.figure(figsize=(20, 10))
table = gridspec.GridSpec(nrows=2, ncols=1, figure=graph, height_ratios=[3,1])

# 1

graph_sup = plt.subplot(table[0, 0])
graph_sup.plot(data, label = 'Close')
graph_sup.set_title("Price")

# 2

graph_inf = plt.subplot(table[1, 0])
graph_inf.plot(data.index, macd, 'b', label='MACD')
graph_inf.plot(data.index, signal, 'r--', label='Signal')
graph_inf.bar(data.index, histogram, color='k')
graph_inf.set_title('MACD')

# Finishing

plt.grid()
plt.show()