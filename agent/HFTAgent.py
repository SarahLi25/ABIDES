# ABIDES/agent/HFTAgent.py
from ABIDES.agent.TradingAgent import TradingAgent

class HFTAgent(TradingAgent):
    """
    High-Frequency Trading Agent for testing:
    - Places buy/sell orders continuously
    - Prints activity to terminal
    """

    def __init__(self, id, name, type, symbol,
                 starting_cash=1000000,
                 order_size=50,
                 wakeup_interval=10_000,
                 **kwargs):
        super().__init__(id, name, type, starting_cash=starting_cash, **kwargs)
        self.symbol = symbol
        self.order_size = order_size
        self.wakeup_interval = wakeup_interval

        # Schedule first wakeup immediately
        self.setWakeup(0)

    def wakeup(self, current_time):
        super().wakeup(current_time)
        # Immediately place buy and sell orders for testing
        bid = 100  # placeholder bid price
        ask = 101  # placeholder ask price
        self.placeLimitOrder(self.symbol, self.order_size, True, ask)
        self.placeLimitOrder(self.symbol, self.order_size, False, bid)
        print(f"[{current_time}] HFTAgent BUY {self.order_size} at {ask}, SELL {self.order_size} at {bid}")
        # Schedule next wakeup
        self.setWakeup(current_time + self.wakeup_interval)

    def receiveMessage(self, current_time, msg):
        super().receiveMessage(current_time, msg)
        # Messages are ignored for this test — all activity forced in wakeup
