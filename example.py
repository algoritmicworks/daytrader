from daytrader import *


def print_values_for_a_coin(trader: Daytrader, token_name: str, interval: Intervals) -> None:
    print(token_name, "| vwap: ", trader.vwap(token_name=token_name, interval=interval))
    print(token_name, "| adl: ", trader.adl(token_name=token_name, interval=interval))
    print(token_name, "| macd: ", trader.macd(token_name=token_name, interval=interval))
    print(token_name, "| rsi: ", trader.rsi(token_name=token_name, interval=interval))
    print(token_name, "| cci: ", trader.cci(token_name=token_name, interval=interval))
    print(token_name, "| fi: ", trader.fi(token_name=token_name, interval=interval))
    print(token_name, "| atr: ", trader.atr(token_name=token_name, interval=interval))
    print(token_name, "| kst: ", trader.kst(token_name=token_name, interval=interval))
    print(token_name, "| trix: ", trader.trix(token_name=token_name, interval=interval))
    print(token_name, "| obv: ", trader.obv(token_name=token_name, interval=interval))

def main():
    algotrader = Daytrader(access_token="1337")
    print_values_for_a_coin(
        trader=algotrader,
        token_name="BTCUSDT",
        interval=Intervals.DAY
    )
    print_values_for_a_coin(
        trader=algotrader,
        token_name="LUNAUSDT",
        interval=Intervals.DAY
    )
    print_values_for_a_coin(
        trader=algotrader,
        token_name="PEPEUSDT",
        interval=Intervals.DAY
    )
main()