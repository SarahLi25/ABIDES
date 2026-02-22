# Import numpy for basic math (average and standard deviation)
import numpy as np
# Import the base TradingAgent class from ABIDES
from ABIDES.agent.TradingAgent import TradingAgent

# Define your Stat Arb Agent by subclassing TradingAgent
class StatArbAgent(TradingAgent):
    """
    Statistical Arbitrage Agent:
    - Buys when price is unusually low
    - Sells when price is unusually high
    Uses a rolling window of recent prices.
    """

    def __init__(self, id, name, type, symbol,
                 starting_cash=1000000,  # How much cash the agent starts with
                 window=20,               # How many past prices to track
                 threshold=1.5,           # Z-score threshold to trigger trades
                 wakeup_interval=500_000_000,  # How often agent checks prices
                 **kwargs):               # Extra parameters for ABIDES
        # Initialize the parent class
        super().__init__(id, name, type, starting_cash=starting_cash, **kwargs)
        self.symbol = symbol       # Which stock/symbol this agent trades
        self.window = window       # Rolling window size
        self.threshold = threshold # Z-score threshold
        self.wakeup_interval = wakeup_interval
        self.prices = []           # Store recent mid-prices

    # Called by ABIDES at each scheduled wakeup
    def wakeup(self, current_time):
        super().wakeup(current_time)
        # Ask the exchange for current bid/ask prices
        self.getCurrentSpread(self.symbol)
        # Schedule next wakeup
        self.setWakeup(current_time + self.wakeup_interval)

    # Called when the agent receives messages (e.g., prices)
    def receiveMessage(self, current_time, msg):
        super().receiveMessage(current_time, msg)

        # Check if this message contains bid/ask prices
        if msg.body.get("msg") == "QUERY_SPREAD":
            bid = msg.body.get("bid")
            ask = msg.body.get("ask")

            if bid and ask:
                # Compute mid-price
                mid_price = (bid + ask) / 2
                # Add to our price history
                self.prices.append(mid_price)

                # Keep only the last 'window' prices
                if len(self.prices) > self.window:
                    self.prices.pop(0)

                # If we have enough prices, calculate mean and std
                if len(self.prices) == self.window:
                    mean = np.mean(self.prices)
                    std = np.std(self.prices)

                    if std > 0:  # Avoid division by zero
                        z = (mid_price - mean) / std  # Calculate z-score

                        # Buy if price is unusually low
                        if z < -self.threshold:
                            self.placeLimitOrder(self.symbol, 100, True, ask)
                        # Sell if price is unusually high
                        elif z > self.threshold:
                            self.placeLimitOrder(self.symbol, 100, False, bid)


