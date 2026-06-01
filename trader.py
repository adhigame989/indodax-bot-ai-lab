import ccxt
import time
import threading
import json
import os
import config
import history
import scanner
import telegram_bot
from paper_wallet import get_balance, reduce_balance

BOT_RUNNING = False

exchange = ccxt.indodax({
    "apiKey": config.API_KEY,
    "secret": config.SECRET_KEY,
    "enableRateLimit": True
})

active_trade = None
trade_file = "active_trade.json"


def save_trade():
    global active_trade
    try:
        with open(trade_file, "w") as f:
            json.dump(active_trade, f)
    except Exception as e:
        print("SAVE TRADE ERROR:", str(e))


def load_trade():
    global active_trade
    try:
        if os.path.exists(trade_file):
            with open(trade_file, "r") as f:
                active_trade = json.load(f)
            print("TRADE LOADED")
    except Exception as e:
        print("LOAD TRADE ERROR:", str(e))


def clear_trade():
    global active_trade
    active_trade = None

    try:
        if os.path.exists(trade_file):
            os.remove(trade_file)
    except Exception as e:
        print("CLEAR TRADE ERROR:", str(e))


def get_trade_amount(balance):
    try:
        compound_size = balance * (config.COMPOUND_PERCENT / 100)

        amount = max(
            config.BASE_TRADE_AMOUNT,
            compound_size
        )

        amount = min(
            amount,
            config.MAX_TRADE_AMOUNT
        )

        return amount

    except Exception as e:
        print("TRADE AMOUNT ERROR:", str(e))
        return config.BASE_TRADE_AMOUNT


# RAPID VERSION NOTE:
# buy_coin(), sell_coin(), monitor_trade(), trade_loop()
# masih menggunakan logic asli.
# Yang dirapikan dulu hanya struktur awal file.
