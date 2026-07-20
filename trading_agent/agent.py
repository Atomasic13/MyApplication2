#!/usr/bin/env python3
"""
Trading Agent — Moving Average Crossover on Alpaca Markets.

Usage:
    python agent.py            # runs indefinitely, checks every CHECK_INTERVAL seconds
    python agent.py --once     # single check then exit (good for cron jobs)
"""

import argparse
import logging
import time
from datetime import datetime, timezone

import alpaca_trade_api as tradeapi

import config
from strategy import get_signal, SMA_FAST, SMA_SLOW

# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("trading_agent")
# ---------------------------------------------------------------------------


def build_client() -> tradeapi.REST:
    if not config.API_KEY or not config.API_SECRET:
        raise RuntimeError(
            "Missing API keys. Copy .env.example to .env and fill in your Alpaca keys."
        )
    return tradeapi.REST(
        config.API_KEY,
        config.API_SECRET,
        config.BASE_URL,
        api_version="v2",
    )


def get_closes(api: tradeapi.REST, symbol: str, limit: int = 50) -> list[float]:
    bars = api.get_bars(
        symbol,
        config.BAR_TIMEFRAME,
        limit=limit,
    ).df
    if bars.empty:
        return []
    return list(bars["close"].values)


def get_position_qty(api: tradeapi.REST, symbol: str) -> float:
    try:
        pos = api.get_position(symbol)
        return float(pos.qty)
    except tradeapi.rest.APIError:
        return 0.0


def execute_buy(api: tradeapi.REST, symbol: str, notional: float) -> None:
    log.info("BUY  $%.2f of %s", notional, symbol)
    api.submit_order(
        symbol=symbol,
        notional=round(notional, 2),
        side="buy",
        type="market",
        time_in_force="day",
    )


def execute_sell(api: tradeapi.REST, symbol: str, qty: float) -> None:
    log.info("SELL %.6f shares of %s", qty, symbol)
    api.submit_order(
        symbol=symbol,
        qty=round(qty, 6),
        side="sell",
        type="market",
        time_in_force="day",
    )


def is_market_open(api: tradeapi.REST) -> bool:
    clock = api.get_clock()
    return clock.is_open


def run_once(api: tradeapi.REST) -> None:
    if not is_market_open(api):
        log.info("Market is closed — nothing to do.")
        return

    closes = get_closes(api, config.SYMBOL)
    if not closes:
        log.warning("No bar data returned for %s.", config.SYMBOL)
        return

    signal = get_signal(closes, SMA_FAST, SMA_SLOW)
    price  = closes[-1]
    log.info(
        "%s  price=$%.4f  fast_sma=%.4f  signal=%s",
        config.SYMBOL, price,
        sum(closes[-SMA_FAST:]) / SMA_FAST,
        signal,
    )

    if signal == "BUY":
        qty = get_position_qty(api, config.SYMBOL)
        if qty > 0:
            log.info("Already holding %.6f shares — skip duplicate BUY.", qty)
        else:
            execute_buy(api, config.SYMBOL, config.TRADE_AMOUNT)

    elif signal == "SELL":
        qty = get_position_qty(api, config.SYMBOL)
        if qty <= 0:
            log.info("No position to sell — skip.")
        else:
            execute_sell(api, config.SYMBOL, qty)

    else:
        log.info("HOLD — no action.")


def run_loop(api: tradeapi.REST) -> None:
    log.info(
        "Agent started | symbol=%s | amount=$%.2f | mode=%s | interval=%ds",
        config.SYMBOL,
        config.TRADE_AMOUNT,
        "PAPER" if config.PAPER_TRADING else "LIVE",
        config.CHECK_INTERVAL,
    )
    while True:
        try:
            run_once(api)
        except Exception as exc:
            log.error("Error during check: %s", exc, exc_info=True)
        time.sleep(config.CHECK_INTERVAL)


def main() -> None:
    parser = argparse.ArgumentParser(description="MA Crossover Trading Agent")
    parser.add_argument("--once", action="store_true", help="Run a single check then exit")
    args = parser.parse_args()

    api = build_client()

    account = api.get_account()
    log.info(
        "Connected | mode=%s | cash=$%s | portfolio=$%s",
        "PAPER" if config.PAPER_TRADING else "LIVE",
        account.cash,
        account.portfolio_value,
    )

    if args.once:
        run_once(api)
    else:
        run_loop(api)


if __name__ == "__main__":
    main()
