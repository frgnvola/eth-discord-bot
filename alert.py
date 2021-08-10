import ccxt, yfinance, pandas_ta as ta, pandas as pd, requests
exchange = ccxt.binance()
message = ""

WEBHOOK_STOCKS_URL = "https://discordapp.com/api/webhooks/870028234312523876/2Rw0-I8LKCS5pEIgXkHtx0tAKiTjEsf37iu21udcGOLWD3nzqaCFMiY2oAKnTAYqP_40"
WEBHOOK_GENERAL_URL = "https://discordapp.com/api/webhooks/870042047795576853/mcQP_Wt3us18HgcNguLnF3-HnCqqjHRNIhGSSzA_hMx_Lipu_u_J3K0ZSk1FWSJJTnop"
STENCHPREET_URL = "https://pbs.twimg.com/profile_images/532700911714729984/T1TYuL-S.jpeg"
GANDALF_URL = "https://static.wixstatic.com/media/065e6b_dd1a8624bd5b40c9848aeec671ed811b.png/v1/fit/w_936%2Ch_733%2Cal_c/file.png"
PEREGRIN_URL = "https://i.pinimg.com/originals/3b/44/c1/3b44c1b3c5be7dda5cd666d16196cd49.jpg"


bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)
rsi = df.ta.rsi()

df = pd.concat([df, adx, macd, rsi], axis=1)

last_row = df.iloc[-1]
print(last_row)

if last_row['ADX_14'] >= 25:
    if last_row['DMP_14'] > last_row['DMN_14']:
        message = f"STRONG UPTREND: Ethereum ADX is {last_row['ADX_14']:.2f}"
    if last_row['DMP_14'] < last_row['DMN_14']:
        message = f"STRONG DOWNTREND: Ethereum ADX is {last_row['ADX_14']:.2f}"

if last_row['ADX_14'] < 25:
    message = f"NO TREND: Ethereum ADX is {last_row['ADX_14']:.2f}"
   
payload = {
    "username": "Gandalf",
    "avatar_url": GANDALF_URL,
    "content": "<@643698753743880204>, get back to the citadel!" 
}
requests.post(WEBHOOK_GENERAL_URL, json=payload)

