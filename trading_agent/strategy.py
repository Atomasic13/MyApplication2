"""
Moving Average Crossover strategy.

Signal logic:
  BUY  when fast SMA crosses ABOVE slow SMA (uptrend starting)
  SELL when fast SMA crosses BELOW slow SMA (downtrend starting)
  HOLD otherwise
"""

from typing import Literal


Signal = Literal["BUY", "SELL", "HOLD"]


def sma(prices: list[float], window: int) -> float | None:
    if len(prices) < window:
        return None
    return sum(prices[-window:]) / window


def get_signal(closes: list[float], fast: int, slow: int) -> Signal:
    """
    Requires at least `slow + 1` bars to detect a crossover.
    Returns HOLD if there is not enough data.
    """
    if len(closes) < slow + 1:
        return "HOLD"

    fast_now  = sma(closes, fast)
    slow_now  = sma(closes, slow)
    fast_prev = sma(closes[:-1], fast)
    slow_prev = sma(closes[:-1], slow)

    if None in (fast_now, slow_now, fast_prev, slow_prev):
        return "HOLD"

    crossed_above = fast_prev <= slow_prev and fast_now > slow_now
    crossed_below = fast_prev >= slow_prev and fast_now < slow_now

    if crossed_above:
        return "BUY"
    if crossed_below:
        return "SELL"
    return "HOLD"
