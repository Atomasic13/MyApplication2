# Trading Agent

A Python trading bot using a **Moving Average Crossover** strategy on [Alpaca Markets](https://alpaca.markets).

## How it works

Every 60 seconds the agent:
1. Fetches the last 50 1-minute bars for your chosen symbol
2. Computes a 9-bar and 21-bar Simple Moving Average (SMA)
3. **BUYs** when the fast SMA crosses above the slow SMA (uptrend signal)
4. **SELLs** your full position when the fast SMA crosses below (downtrend signal)
5. Logs every decision — nothing happens silently

---

## Quick start (5 minutes)

### 1. Get free Alpaca API keys
1. Go to [alpaca.markets](https://alpaca.markets) and create a free account
2. Click **Paper Trading** in the sidebar
3. Click **Your API Keys** → Generate Key
4. Copy the key and secret

### 2. Set up the agent
```bash
cd trading_agent

# Install dependencies
pip install -r requirements.txt

# Create your config
cp .env.example .env
# Edit .env and paste in your API key + secret
```

### 3. Run in paper mode (fake money, real market data)
```bash
python agent.py
```

Sample output:
```
2026-07-20 14:31:00  INFO      Connected | mode=PAPER | cash=$100000.00 | portfolio=$100000.00
2026-07-20 14:31:01  INFO      AAPL  price=$189.42  fast_sma=189.31  signal=BUY
2026-07-20 14:31:01  INFO      BUY  $1.00 of AAPL
2026-07-20 14:32:01  INFO      AAPL  price=$189.44  fast_sma=189.38  signal=HOLD
2026-07-20 14:32:01  INFO      HOLD — no action.
```

### 4. Switch to real money
When you're happy with paper results, edit `.env`:
```
PAPER_TRADING=false
TRADE_AMOUNT=1.00   # your actual $1
```

---

## Configuration (`.env`)

| Variable | Default | Description |
|---|---|---|
| `ALPACA_API_KEY` | — | Your Alpaca key ID |
| `ALPACA_API_SECRET` | — | Your Alpaca secret key |
| `PAPER_TRADING` | `true` | `false` for real money |
| `SYMBOL` | `AAPL` | Stock ticker to trade |
| `TRADE_AMOUNT` | `1.00` | Dollars per buy (fractional shares) |
| `CHECK_INTERVAL` | `60` | Seconds between signal checks |

## Run as a cron job (single check per minute)
```bash
# In your crontab:
* * * * * /usr/bin/python3 /path/to/trading_agent/agent.py --once >> /var/log/trader.log 2>&1
```

---

## Risk warning
This is a simple educational bot. Past performance of any strategy does not guarantee future results. Only trade money you can afford to lose.
