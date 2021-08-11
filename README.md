## Eth-Discord-Bot

## Project Overview
Implement a python bot that collects price data for Ethereum and generates uptrend/downtrend signals to send to your Discord channel.
This project was largely guided and inspired by the YouTube series of a much better programmer. Please look through his GitHub and YouTube for similar cryptocurrency/stock market projects in python.
 - [YouTube Channel](https://www.youtube.com/channel/UCY2ifv8iH1Dsgjrz-h3lWLQ)
 - [Github](https://github.com/hackingthemarkets)



## Libraries, Frameworks, Packages used
#### Binance CCXT
- The CCXT library has 'exchange' classes from which we obtain price data
- [Learn More about the Binance CCXT library](https://ccxt.readthedocs.io/en/latest/manual.html)

#### Pandas and Pandas_ta
- Both are needed for data manipulation and storage in DataFrame classes, Pandas_ta has technical analysis specific functions that make appending useful data to dataframes very easy 
- [Learn more about the pandas library](https://pandas.pydata.org/docs/)
- [Learn more about the pandas_ta library](https://github.com/twopirllc/pandas-ta)

#### Requests
- Used to post message in discord with json data, Requests is a simple HTTP library
- [Learn more about the requests library](https://docs.python-requests.org/en/master/user/install/)






