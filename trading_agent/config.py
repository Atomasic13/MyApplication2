import os
from dotenv import load_dotenv

load_dotenv()

# --- Alpaca API credentials ---
# Get free keys at https://alpaca.markets
API_KEY    = os.getenv("ALPACA_API_KEY", "")
API_SECRET = os.getenv("ALPACA_API_SECRET", "")

# Paper trading = fake money, real market data (safe to start)
# Live trading  = real money
PAPER_TRADING = os.getenv("PAPER_TRADING", "true").lower() != "false"

BASE_URL = (
    "https://paper-api.alpaca.markets"
    if PAPER_TRADING
    else "https://api.alpaca.markets"
)

# --- Trading parameters ---
SYMBOL          = os.getenv("SYMBOL", "AAPL")   # stock to trade
TRADE_AMOUNT    = float(os.getenv("TRADE_AMOUNT", "1.00"))  # dollars per trade (fractional)
CHECK_INTERVAL  = int(os.getenv("CHECK_INTERVAL", "60"))    # seconds between checks

# Moving average windows (bars)
SMA_FAST = 9
SMA_SLOW = 21
BAR_TIMEFRAME = "1Min"   # 1Min, 5Min, 15Min, 1Hour, 1Day
