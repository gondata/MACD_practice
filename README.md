# MACD

This repository contains a Python script to obtain and analyze the stock price data of NIO Inc. The script uses the Yahoo Finance API to retrieve the data, and then calculates the Exponential Moving Averages (EMA), Moving Average Convergence Divergence (MACD) and Histogram. Finally, it creates a graph with the stock prices and the MACD indicators.

## Prerequisites

To run this script, you need to have Python 3 installed on your machine. You also need to have the following packages installed:

- pandas
- numpy
- yfinance
- matplotlib

You can install these packages by running:

```

pip install -r requirements.txt

```

## Getting the Data

To get the data, the script uses the Yahoo Finance API. You can change the **`ticker`**, **`startdate`**, and **`enddate`** variables to obtain the data for a different stock or period.

```

ticker = ['NIO']
startdate = '2020-01-01'
enddate = '2023-03-08'

data = pdr.get_data_yahoo(ticker, start=startdate, end=enddate)['Adj Close']

```

## Calculating the Indicators

The script calculates the Exponential Moving Averages (EMA), Moving Average Convergence Divergence (MACD), and Histogram using the **`ewm`** method from pandas.

```

ewm_fast = data.ewm(span=12, adjust=False).mean()
ewm_slow = data.ewm(span=26, adjust=False).mean()

macd = ewm_fast - ewm_slow
signal = macd.ewm(span=9, adjust=False).mean()
histogram = macd - signal

```

## Creating the Graph

The script creates a graph using the **`matplotlib`** library. The graph shows the stock prices and the MACD indicators.

```

graph = plt.figure(figsize=(20, 10))
table = gridspec.GridSpec(nrows=2, ncols=1, figure=graph, height_ratios=[3,1])

graph_sup = plt.subplot(table[0, 0])
graph_sup.plot(data, label = 'Close')
graph_sup.set_title("Price")

graph_inf = plt.subplot(table[1, 0])
graph_inf.plot(data.index, macd, 'b', label='MACD')
graph_inf.plot(data.index, signal, 'r--', label='Signal')
graph_inf.bar(data.index, histogram, color='k')
graph_inf.set_title('MACD')

plt.grid()
plt.show()

```

## Running the Script

To run the script, open a terminal window and navigate to the directory where the script is located. Then, run the following command:

```

python nio_analysis.py

```
