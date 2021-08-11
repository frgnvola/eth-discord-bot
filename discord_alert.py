import ccxt, yfinance, pandas_ta as ta, pandas as pd, requests
exchange = ccxt.binance()
message = ""


# See Discord API for details on obtaining Webhook URLs. Unique URL for each channels 
WEBHOOK_STOCKS_URL = "https://discordapp.com/api/webhooks/870028234312523876/2Rw0-I8LKCS5pEIgXkHtx0tAKiTjEsf37iu21udcGOLWD3nzqaCFMiY2oAKnTAYqP_40"
WEBHOOK_GENERAL_URL = "https://discordapp.com/api/webhooks/870042047795576853/mcQP_Wt3us18HgcNguLnF3-HnCqqjHRNIhGSSzA_hMx_Lipu_u_J3K0ZSk1FWSJJTnop"

# Bot Profile Picture
BOT_IMG_URL = "https://static.wixstatic.com/media/065e6b_dd1a8624bd5b40c9848aeec671ed811b.png/v1/fit/w_936%2Ch_733%2Cal_c/file.png"

# Pull ETH price for a 5m period, over the last 500 periods.
bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)

# Pass bars (ETH Price data) to a Pandas Dataframe with matching columns
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])

# Using TA-library, get and append useful data columns to dataframe for price action analysis
adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)
rsi = df.ta.rsi()
df = pd.concat([df, adx, macd, rsi], axis=1)

# Obtain last row of df for most recent indicator data, compare to static thresholds
    # TODO: make thresholds dynamic? --> compare to last n (or just nth) in each respective column
        # most likely need different threshold event types for differnet indicators, i.e. seperate functions
last_row = df.iloc[-1]

if last_row['ADX_14'] >= 25:
    if last_row['DMP_14'] > last_row['DMN_14']:
        message = f"STRONG UPTREND: Ethereum ADX is {last_row['ADX_14']:.2f}"
    if last_row['DMP_14'] < last_row['DMN_14']:
        message = f"STRONG DOWNTREND: Ethereum ADX is {last_row['ADX_14']:.2f}"

if last_row['ADX_14'] < 25:
    message = f"NO TREND: Ethereum ADX is {last_row['ADX_14']:.2f}"
   
# Create formated json message 
payload = {
    "username": "Gandalf Bot",
    "avatar_url": BOT_IMG_URL,
    "content": message
}
# Post the message: need Webhook URL and json message
requests.post(WEBHOOK_GENERAL_URL, json=payload)

