
# Simulation settings
simulation = {
    "start_time": "09:30:00",  # Market opens at 9:30 AM
    "end_time": "16:00:00",    # Market closes at 4:00 PM
    "seed": 1                  # Random seed for reproducibility
}

# Agents in this simulation
agents = [
    {
        "type": "ABIDES.agent.MarketMakerAgent.MarketMakerAgent",  # Built-in ABIDES MarketMaker
        "name": "mm",                                              # Agent name
        "num_agents": 3,                                          # Number of market makers
        "config": {
            "symbol": "AAPL",                                     # Stock to provide liquidity for
            "starting_cash": 1000000,                             # Cash to start with
            "wakeup_interval": 1000000000                          # How often they adjust prices
        }
    }
]

# Logging settings
logging = {
    "csv_path": "HighVol/MMTrials/rep1/mm_log.csv",  # Where to save output CSV
    "log_orders": True,                              # Log order activity
    "log_messages": True,                            # Log messages received
    "log_events": True                               # Log market events
}