import time

import ccxt
from ccxt.base.errors import NetworkError, RequestTimeout

# Instanciting Binance
binance_ex = ccxt.binance()
binance_ex.load_markets()


# asset data integration with ccxt
def asset_data_integrator(symbol):
    asset_data = {}
    funding_post_fix = symbol.split("/")[-1]
    f_symbol = f"{symbol}:{funding_post_fix}"

    def exchange_data(symbol):
        funding_rate_ = binance_ex.fetch_funding_rate(f_symbol)

        open_interest_ = binance_ex.fetch_open_interest_history(
            f_symbol, "12h", limit=1
        )[-1]
        price_dict = binance_ex.fetch_ticker(symbol)

        return funding_rate_, open_interest_, price_dict

    try:
        asset_data = {}

        funding_rate_, open_interest_, price_dict = exchange_data(symbol)

    except (RequestTimeout, NetworkError) as e:
        time.sleep(3)
        asset_data = {}

        funding_rate_, open_interest_, price_dict = exchange_data(symbol)

    finally:
        asset_data["price_change"] = price_dict["info"]["priceChange"]
        asset_data["price"] = price_dict["close"]
        asset_data["volume"] = price_dict["info"]["volume"]
        asset_data["open_interest"] = open_interest_["openInterestAmount"]
        asset_data["funding_rate"] = funding_rate_["fundingRate"]
    return asset_data


print(asset_data_integrator("BTC/USDT"))
