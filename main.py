from algotrader.algotrader import Algotrader, Intervals


def print_values_for_a_coin(trader: Algotrader, token_name: str, interval: Intervals) -> None:
    print("vwap: ", trader.vwap(token_name=token_name, interval=interval))
    print("adl: ", trader.adl(token_name=token_name, interval=interval))
    print("macd: ", trader.macd(token_name=token_name, interval=interval))
    print("rsi: ", trader.rsi(token_name=token_name, interval=interval))
    print("cci: ", trader.cci(token_name=token_name, interval=interval))
    print("fi: ", trader.fi(token_name=token_name, interval=interval))
    print("atr: ", trader.atr(token_name=token_name, interval=interval))
    print("kst: ", trader.kst(token_name=token_name, interval=interval))
    print("trix: ", trader.trix(token_name=token_name, interval=interval))
    print("obv: ", trader.obv(token_name=token_name, interval=interval))

def main():
    algotrader = Algotrader(access_token="1337")
    print_values_for_a_coin(
        trader=algotrader,
        token_name="BTCUSDT",
        interval=Intervals.DAY
    )
main()