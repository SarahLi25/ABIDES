
# Simulation settings
simulation = {
    "start_time": "09:30:00",  # Market opens at 9:30 AM
    "end_time": "16:00:00",    # Market closes at 4:00 PM
    "seed": 1                  # Random seed for reproducibility
}

# Agents in this simulation
agents = [
    {
        "type": "ABIDES.agent.StatArbAgent.StatArbAgent",  # The Stat Arb class in ABIDES/agent/
        "name": "statarb",                                 # Name of this agent
        "num_agents": 3,                                   # Number of identical agents
        "config": {
            "symbol": "AAPL",                              # Which stock to trade
            "starting_cash": 1000000,                      # Initial cash
            "window": 20,                                  # Rolling price window for statistics
            "threshold": 1.5,                              # Z-score threshold to trigger trades
            "wakeup_interval": 500000000                   # How often the agent checks market
        }
    }
]

# Logging settings
logging = {
    "csv_path": "HighVol/StatArbTrials/rep1/stat_arb_log.csv",  # Where to save output CSV
    "log_orders": True,                                        # Log order activity
    "log_messages": True,                                      # Log messages received
    "log_events": True                                         # Log market events
}