from binance.client import Client
import pickle

client = Client('XXX', 'YYY') # Insted of XXX and YYY you should use your API key and secret
klines = client.get_historical_klines("WAVESBTC", Client.KLINE_INTERVAL_1MINUTE, "21 Nov, 2018")

with open('data_file', 'wb') as fp:
    pickle.dump(klines, fp)
fp.close()
