#!/usr/bin/python
#Author: egely1337
#Date: 10/4/2023

import requests
from .util import *

REQUEST_TIMEOUT = 10

class Daytrader:
    def __init__(self, access_token: str):
        if access_token == None: raise Exception("Daytrader needs a access token to work!")
        self.access_token = access_token
    
    def rsi(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY
    ) -> float:
        """Gets RSI value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createRsi(token_name=token_name, interval=interval.value),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j = r.json()

            if j.get("status"):
                return float(j.get("realTimeRsi"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e
    
    def macd(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY
    ) -> float:
        """Gets MACD value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createMacd(token_name=token_name, interval=interval.value),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeMacd"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e

    def cci(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY
    ) -> float:
        """Gets CCI value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createCci(token_name=token_name, interval=interval.value),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeCci"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e

    def adl(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY
    ) -> float:
        """Gets ADL value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createAdl(token_name=token_name, interval=interval.value),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeAdl"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e
        
    def fi(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY
    ) -> float:
        """Gets FI value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createFi(token_name=token_name, interval=interval.value),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeFi"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e
        
    def atr(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY
    ) -> float:
        """Gets ATR value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createAtr(token_name=token_name, interval=interval.value),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeAtr"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e
    
    def trix(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY
    ) -> float:
        """Gets TRIX value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createTrix(token_name=token_name, interval=interval.value),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeTrix"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e
        
    def obv(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY
    ) -> float:
        """Gets OBV value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createObv(token_name=token_name, interval=interval.value),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeObv"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e
        
    def kst(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY
    ) -> float:
        """Gets KST value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createKst(token_name=token_name, interval=interval.value),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeStochasticKst"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e
        
    
    def vwap(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY
    ) -> float:
        """Gets VWAP value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createVwap(token_name=token_name, interval=interval.value),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeVwap"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e
    
    def sma(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY,
        period: int = 20
    ) -> float:
        """Gets SMA value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createSma(token_name=token_name, interval=interval.value, period=period),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeSma"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e

    def ema(
        self,
        token_name: str = "BTCUSDT",
        interval: Intervals = Intervals.DAY,
        period: int = 20
    ) -> float:
        """Gets EMA value for a token eg. "BTCUSDT" """
        try:
            r = requests.get(
                url=CreateUrl.createEma(token_name=token_name, interval=interval.value, period=period),
                headers={
                    "Authorizaton" : self.access_token
                },
                timeout=REQUEST_TIMEOUT
            )
            j: dict = r.json()

            if j.get("status"):
                return float(j.get("realTimeEma"))
            else:
                raise Exception("A problem occured")

        except Exception as e:
            raise e
        