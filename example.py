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
    daytrader = Daytrader(access_token="1337") # create a instance of class Daytrader and put access_token to the class which we gave

    while True:
        try:
            BTCUSDT_RSI = daytrader.rsi(token_name="BTCUSDT", interval=Intervals.DAY)
            if BTCUSDT_RSI < 35:
                print("long", BTCUSDT_RSI)
            elif BTCUSDT_RSI > 65:
                print("short", BTCUSDT_RSI)
            else:
                print("hold", BTCUSDT_RSI)
        except KeyboardInterrupt:
            break
        except Exception as e: 
            pass

if __name__ == "__main__":
    main() # run main 