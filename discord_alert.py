import ccxt, yfinance, pandas_ta as ta, pandas as pd, requests
exchange = ccxt.binance()
message = ""

WEBHOOK_STOCKS_URL = "https://discordapp.com/api/webhooks/870028234312523876/2Rw0-I8LKCS5pEIgXkHtx0tAKiTjEsf37iu21udcGOLWD3nzqaCFMiY2oAKnTAYqP_40"
WEBHOOK_GENERAL_URL = "https://discordapp.com/api/webhooks/870042047795576853/mcQP_Wt3us18HgcNguLnF3-HnCqqjHRNIhGSSzA_hMx_Lipu_u_J3K0ZSk1FWSJJTnop"

BOT_IMG_URL = "https://static.wixstatic.com/media/065e6b_dd1a8624bd5b40c9848aeec671ed811b.png/v1/fit/w_936%2Ch_733%2Cal_c/file.png"


bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)
rsi = df.ta.rsi()

df = pd.concat([df, adx, macd, rsi], axis=1)

last_row = df.iloc[-1]

if last_row['ADX_14'] >= 25:
    if last_row['DMP_14'] > last_row['DMN_14']:
        message = f"STRONG UPTREND: Ethereum ADX is {last_row['ADX_14']:.2f}"
    if last_row['DMP_14'] < last_row['DMN_14']:
        message = f"STRONG DOWNTREND: Ethereum ADX is {last_row['ADX_14']:.2f}"

if last_row['ADX_14'] < 25:
    message = f"NO TREND: Ethereum ADX is {last_row['ADX_14']:.2f}"
   
payload = {
    "username": "Gandalf Bot",
    "avatar_url": BOT_IMG_URL,
    "content": message
}
requests.post(WEBHOOK_GENERAL_URL, json=payload)

