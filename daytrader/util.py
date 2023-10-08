from enum import Enum

class Url(Enum):
    BASE_URL = "http://13.53.214.72/api/v1" # currently private

    RSI_URL = f"{BASE_URL}/rsi"
    MACD_URL = f"{BASE_URL}/macd"
    CCI_URL = f"{BASE_URL}/cci"
    ADL_URL = f"{BASE_URL}/adl"
    FI_URL = f"{BASE_URL}/fi"
    ATR_URL = f"{BASE_URL}/atr"
    KST_URL = f"{BASE_URL}/kst"
    TRIX_URL = f"{BASE_URL}/trix"
    OBV_URL = f"{BASE_URL}/obv"
    VWAP_URL = f"{BASE_URL}/vwap"
    SMA_URL = f"{BASE_URL}/sma"
    EMA_URL = f"{BASE_URL}/ema"

class Intervals(Enum):
    MONTH = "1M" # 1 month
    WEEK = "1w" # 1 week
    DAY = "1d" # 1 day
    HOUR = "1h" # 1 day
    MINUTE = "1m" # 1 minute
    SIXHOURS = "6h" # 6 hours
    TWOHOURS = "2h" # 2 hours
    THREEHOURS = "3h" # 3 hours
    

class CreateUrl:
    @staticmethod
    def createVwap(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY
    ):
        return f"{Url.VWAP_URL.value}/{token_name}?history={history}&interval={interval}"
    
    def createObv(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY
    ):
        return f"{Url.OBV_URL.value}/{token_name}?history={history}&interval={interval}"
    
    def createRsi(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY
    ):
        return f"{Url.RSI_URL.value}/{token_name}?history={history}&interval={interval}"

    def createMacd(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY
    ):
        return f"{Url.MACD_URL.value}/{token_name}?history={history}&interval={interval}"
    
    def createCci(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY
    ):
        return f"{Url.CCI_URL.value}/{token_name}?history={history}&interval={interval}"

    def createAdl(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY
    ):
        return f"{Url.ADL_URL.value}/{token_name}?history={history}&interval={interval}"
    
    def createFi(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY
    ):
        return f"{Url.FI_URL.value}/{token_name}?history={history}&interval={interval}"
    
    def createAtr(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY
    ):
        return f"{Url.ATR_URL.value}/{token_name}?history={history}&interval={interval}"
    
    def createKst(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY
    ):
        return f"{Url.KST_URL.value}/{token_name}?history={history}&interval={interval}"

    def createTrix(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY
    ):
        return f"{Url.TRIX_URL.value}/{token_name}?history={history}&interval={interval}"

    def createSma(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY,
        period: int = 20
    ):
        return f"{Url.SMA_URL.value}/{token_name}?history={history}&interval={interval}&period={period}"

    def createEma(
        token_name:str = "BTCUSDT",
        history: int = 1,
        interval: Intervals = Intervals.DAY,
        period: int = 20
    ):
        return f"{Url.EMA_URL.value}/{token_name}?history={history}&interval={interval}&period={period}"